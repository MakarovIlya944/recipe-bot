from src.scrappers.scrapper import Scrapper
from src.scrappers.edimdoma import ScrapperEdimDoma
from src.model import BotDatabase

class Shef():
  
  scrapper:Scrapper = ScrapperEdimDoma
  db:BotDatabase = None
  
  def __init__(self, scrapper="EdimDoma") -> None:
    super().__init__()
    if scrapper == "EdimDoma":
      self.scrapper = ScrapperEdimDoma
    
  def connect(provider='sqlite', user='', password='', host='', database='recipes') -> None:
    Shef.db = BotDatabase(provider)
  
  def scrap() -> int:
    count = 0
    err_count = 0
    for word in Shef.scrapper.base_words:
      print(f'Scrap {word}')
      res = Shef.db.add_recieps(Shef.scrapper.scrap(Shef.scrapper, word))
      count += res[0]
      err_count += res[1]
    return count, err_count
      
  def save(self) -> None:
    pass
  
  def get(recipe: str, with_ingredient: str=None, without_ingredient: str=None) -> dict:
    r = Shef.db.get_recipe(recipe, with_ingredient, without_ingredient)[0]
    return Shef.db.parse_recipe(r)