from pony.orm import Database, Required, Optional

db = Database()

class BotDatabase():
    
    def __init__(self) -> None:
        pass

    class Recipe(db.Entity):
        name = Required(str)
        descr = Optional(str)
        ingredients = Required(str)
        steps = Required(str)
        