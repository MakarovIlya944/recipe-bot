from pony.orm import Database, Required, Optional, db_session, PrimaryKey, Set, select, get

class BotDatabase():
    db = Database()

    class Reciep(db.Entity):
        recipeid = PrimaryKey(int, auto=True)
        name = Required(str)
        desc = Optional(str)
        ingredients = Set('IngredientMeasured')
        steps = Required(str)
        baseword = Required(str)
        
    class Ingredient(db.Entity):
        ingredientid = PrimaryKey(int, auto=True)
        imeasuredids = Set('IngredientMeasured')
        name = Required(str)
        
    class IngredientMeasured(db.Entity):
        imeasuredid = PrimaryKey(int, auto=True)
        ingredient = Required('Ingredient')
        measuretitile = Required(str)
        measurenumber = Required(int)
        recipes = Set('Reciep')
        
    def __init__(self, provider='sqlite', user='', password='', host='', database='recipes') -> None:
        if provider == "sqlite":
            self.db.bind(provider='sqlite', filename='recipes.sqlite', create_db=True)
        elif provider == "postgres":
            self.db.bind(provider, user, password, host, database)
            
        self.db.generate_mapping(create_tables=True)
        
    def __get_or_create_Ingredient(self, name):
        try:
            e = get(ing for ing in BotDatabase.Ingredient if ing.name == name)
        except Exception as ex:
            print(ex.args)
        if e is None:
            return BotDatabase.Ingredient(name=name)
        return e
        
    def __get_or_create_IngredientMeasured(self, ingredient, number, title):
        if not title:
            title = " "
        if not number:
            number = 0
        try:
            e = get(ing for ing in BotDatabase.IngredientMeasured if ing.ingredient == ingredient and ing.measuretitile == title and ing.measurenumber == number)
        except Exception as ex:
            print(ex.args)
        if e is None:
            return BotDatabase.IngredientMeasured(
                        measuretitile=title,
                        measurenumber=number,
                        ingredient=ingredient
                        )
        return e
        
    @db_session
    def add_recieps(self, recieps:list):
        count = 0
        err_count = 0
        for reciep in recieps:
            try:
                ingredients = []
                for i in reciep['ingredients']:
                    ing = self.__get_or_create_Ingredient(i[0])
                    ingredients.append(self.__get_or_create_IngredientMeasured(ing, i[1], i[2]))
                
                r = BotDatabase.Reciep(
                    name=reciep['name'], 
                    desc=reciep['desc'], 
                    ingredients=ingredients, 
                    steps=reciep['steps'], 
                    baseword=reciep['baseword']
                    )
                count += 1
            except Exception as ex:
                print(f'{str(reciep)}: {ex.args}')
                err_count += 1
        return count, err_count
    
    @db_session    
    def get_recipe(self, baseword: str, with_ingredient: str=None, without_ingredient: str=None, limit: int=20)-> tuple:
        if with_ingredient:
            i = select(i for i in BotDatabase.Ingredient if with_ingredient in i.name).first()
            tmp = select(p for p in BotDatabase.Reciep for im in BotDatabase.IngredientMeasured if p.baseword == baseword and im in p.ingredients and im.ingredient == i)
            print([p.to_dict(only='recipeid') for p in tmp])
            return tmp.random(1)
        return select(p for p in BotDatabase.Reciep if p.baseword == baseword).random(1)
        
    @db_session   
    def parse_recipe(self, recipe):
        ingredients = select((i.name, im.measuretitile, im.measurenumber) for im in recipe.ingredients for i in BotDatabase.Ingredient if im.ingredient == i)
        ingredients = [_c for _c in ingredients]
        return {
            "name":recipe.name,
            "desc":recipe.desc,
            "ingredients":ingredients,
            "steps":recipe.steps.split('\n'),
            "baseword":recipe.baseword
        }
        