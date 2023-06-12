from src.scrappers.scrapper import Scrapper
from bs4 import BeautifulSoup
import requests as r
import json
import time

class ScrapperEdimDoma(Scrapper):
  
  base_url = 'https://www.edimdoma.ru'
  recieps_count = 0
  num_recipes=20
  num_pages=10
  
  def __init__(self) -> None:
    super().__init__()
    
  def scrap(self, base_word, with_ingredient=None, without_ingredient=None) -> list:
    return self.__find_recipes(self, base_word, num_recipes=self.num_pages, num_pages=self.num_pages)
  
  def __find_recipes(self, base_word, num_recipes, num_pages) -> list:
    self.recieps_count = 0
    recipes_all = []
    for i in range(num_pages):
      try:
        # https://www.edimdoma.ru/retsepty?direction=&field=&page=2&query=%D0%B7%D0%B0%D0%B2%D1%82%D1%80%D0%B0%D0%BA&user_ids=&with_ingredient=&with_ingredient_condition=and&without_ingredient=
        params = {
          'page' : i,
          'query' : base_word,
        }
        resp = r.get(self.base_url + '/retsepty', params=params)
        soup = BeautifulSoup(resp.text, 'lxml')

        recipes = soup.find_all('article')
        recipes = [i.contents[0].attrs['href'] for i in recipes if i.attrs.get('data-id')]
        recipes = [ self.__parse_reciep(self, u) for u in recipes]
        for rec in recipes:
          rec['baseword'] = base_word
        recipes_all.extend(recipes)

        print(f'recieps: {self.recieps_count}/{num_recipes}')
        print(f'pages: {i}/{num_pages}')
        if self.recieps_count >= num_recipes:
          break
        # print('Saving...')
        # with open(f'data/data_{i}.json', 'w') as f:
        #   f.write(json.dumps(recipes))

        time.sleep(self.timeout_sec)
      except Exception as ex:
        print(ex.args)
    return recipes_all

  def __parse_reciep(self, url) -> dict:
    try:
      step="name"
      resp = r.get(self.base_url + url)
      soup = BeautifulSoup(resp.text, 'lxml')
      
      res = {}
      
      # print(f'#{self.recieps_count}: Creating name...')
      name = soup.find('h1', {"class": "recipe-header__name"}).contents[0]
      res["name"] = name
      
      step="description"
      # print(f'#{self.recieps_count}: Creating desc...')
      description = soup.find('div', {"class": "recipe_description"})
      # description = description.contents[0].contents[0] if description else ""
      try:
        description = description.text
      except Exception as ex:
        raise IndexError(f'Description parse error: {str(ex.args)}') from ex
      if not type(description) is str:
        description = ""
      res["desc"] = description
      
      step="ingredients"
      # print(f'#{self.recieps_count}: Creating ingredients...')
      ingredients = soup.find_all(self.__is_tag_ingredient_title)
      res["ingredients"] = [(i.contents[0].contents[0].contents[1].contents[1].contents[0].text, 
                      i.contents[0].contents[0].contents[1].contents[0].attrs['data-amount'], 
                      i.contents[0].contents[0].contents[1].contents[0].attrs['data-unit-title']) for i in ingredients]
      
      step="steps"
      
      # print(f'#{self.recieps_count}: Creating steps...')
      steps = soup.find_all('div', {"data-module":"step_hint"})
      steps = [s.next for s in steps]
      
      res["steps"] = self.newline.join(steps)
      # print(f'#{recipeCount}: Creating tags...')
      # tags = soup.find_all(IsTagElem)
      # tags = [t.string for t in tags]
      self.recieps_count += 1
      return res
    except Exception as ex:
      print(f'{name}: problem with {step} {str(ex.args)}')

  def __is_tag_ingredient_title(tag):
    return tag.attrs.get('class') and 'definition-list-table__tr' in tag.attrs.get('class') and not ('nutritional-value__nutritional-list' in tag.parent.parent.attrs.get('class'))

if __name__ == '__main__':
  # FindRecipes(1000)
  # with open('data/data_all.json', 'w') as f:
  #   f.write(json.dumps(allRecipies))
  s = ScrapperEdimDoma()
  res = s.scrap(s.base_words[0])
  
  print("done")