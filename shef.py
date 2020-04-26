from bs4 import BeautifulSoup
import requests as r
import json

baseUrl = 'https://www.edimdoma.ru'
recipeCount = 0
allRecipies = []


def IsTagElem(tag):
    return tag.attrs.get('class') and 'button' in tag.attrs.get('class') and 'button_tag' in tag.attrs.get('class')

def IsTagIngredientValue(tag):
    return tag.attrs.get('class') and 'definition-list-table__td_value' in tag.attrs.get('class') and 'definition-list-table__td' in tag.attrs.get('class')

def IsTagIngredientTitle(tag):
    return tag.attrs.get('class') and 'checkbox__input' in tag.attrs.get('class') and 'recipe_ingredient_checkbox' in tag.attrs.get('class')

def GetRecipe(url):
    try:
        global recipeCount
        resp = r.get(baseUrl + url)
        soup = BeautifulSoup(resp.text, 'lxml')
        print(f'#{recipeCount}: Creating steps...')
        steps = soup.find_all('div', id='recipe_steps')[0].contents
        steps = [s.contents[0].contents[2].contents[0].next for s in steps if 'recipe_step' in s.attrs['class']]

        print(f'#{recipeCount}: Creating tags...')
        tags = soup.find_all(IsTagElem)
        tags = [t.string for t in tags]

        print(f'#{recipeCount}: Creating ingredients...')
        ingredients = soup.find_all(IsTagIngredientTitle)
        ingredients = [(i.attrs['data-intredient-title'], i.attrs['data-unit-id'] + i.attrs['data-unit-title']) for i in ingredients]
        title = soup.find_all('h1')[0].contents[0]

        recipeCount += 1
        print(f'#{recipeCount}: Created')
        return {'title':title, 'ingredients':ingredients, 'tags':tags, 'steps':steps}   
    except Exception:
        return {}
    

def FindRecipes(num):
    global allRecipies

    for i in range(num):
        try:
            params = {'page' : i}
            resp = r.get(baseUrl + '/retsepty', params=params)
            soup = BeautifulSoup(resp.text, 'lxml')

            recipes = soup.find_all('article')
            recipes = [i.contents[0].attrs['href'] for i in recipes if i.attrs.get('data-id')]
            recipes = [ GetRecipe(u) for u in recipes]

            print('Saving...')
            with open(f'data/data_{i}.json', 'w') as f:
                f.write(json.dumps(recipes))

            allRecipies.extend(recipes)
        except Exception:
            pass

if __name__ == '__main__':
    FindRecipes(1000)
    with open('data/data_all.json', 'w') as f:
        f.write(json.dumps(allRecipies))