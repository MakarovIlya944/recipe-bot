from src.scrappers.scrapper import Scrapper
from src.scrappers.edimdoma import ScrapperEdimDoma
from src.model import BotDatabase

class Shef():
  
  scrapper:Scrapper = ScrapperEdimDoma
  db:BotDatabase = None
  lastConfig:list[str] = [0,0,0]
  
  def __init__(self, scrapper="EdimDoma") -> None:
    super().__init__()
    if scrapper == "EdimDoma":
      self.scrapper = ScrapperEdimDoma
    
  def connect(provider='sqlite', user='', password='', host='', database='recipes') -> None:
    Shef.db = BotDatabase(provider)
  
  def scrap(**kwargs) -> tuple:
    count = 0
    err_count = 0
    if kwargs.get('num_pages'):
      Shef.scrapper.num_pages = kwargs.get('num_pages')
    if kwargs.get('num_recipes'):
      Shef.scrapper.num_recipes = kwargs.get('num_recipes')
    for word in Shef.scrapper.base_words:
      print(f'Scrap {word}')
      res = Shef.db.add_recieps(Shef.scrapper.scrap(Shef.scrapper, word))
      count += res[0]
      err_count += res[1]
    return (count, err_count)
      
  def save(self) -> None:
    pass
  
  def get(recipe: str, with_ingredient: str=None, without_ingredient: str=None) -> dict:
    Shef.lastConfig[0] = recipe
    Shef.lastConfig[1] = with_ingredient
    Shef.lastConfig[2] = without_ingredient
    return Shef.db.parse_recipe(Shef.db.get_recipe(recipe, with_ingredient, without_ingredient)[0])
  
  def next() -> dict:
    return Shef.db.parse_recipe(Shef.db.get_recipe(Shef.lastConfig[0], Shef.lastConfig[1], Shef.lastConfig[2])[0])