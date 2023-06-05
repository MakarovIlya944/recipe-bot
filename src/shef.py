from src.scrappers.scrapper import Scrapper
from src.scrappers.edimdoma import ScrapperEdimDoma
from src.model import BotDatabase

class Shef():
  
  scrapper:Scrapper = None
  db:BotDatabase = None
  
  def __init__(self, scrapper="EdimDoma") -> None:
    super().__init__()
    if scrapper == "EdimDoma":
      self.scrapper = ScrapperEdimDoma
    
  def connect(self, provider='sqlite', user='', password='', host='', database='recipes') -> None:
    self.db = BotDatabase(provider)
  
  def scrap(self) -> int:
    count = 0
    err_count = 0
    for word in self.scrapper.base_words:
      print(f'Scrap {word}')
      res = self.db.add_recieps(self.scrapper.scrap(self.scrapper, word))
      count += res[0]
      err_count += res[1]
    return count, err_count
      
  def save(self) -> None:
    pass
  
  def get(self, recipe: str, with_ingredient: str=None, without_ingredient: str=None) -> BotDatabase.Reciep:
    return self.db.get_recipe(recipe, with_ingredient, without_ingredient)[0]