from scrapper import Scrapper
from bs4 import BeautifulSoup
import requests as r
import json

recipeCount = 0
allRecipies = []

class ScrapperEdimDoma(Scrapper):
  
  base_url = 'https://www.edimdoma.ru'
  
  def __init__(self) -> None:
    super().__init__()
    
  def scrap(self, base_word, with_ingredient=None, without_ingredient=None) -> list:
    return self.__find_recipes(base_word)
  
  def __find_recipes(self, base_word, num_recipes=100, num_pages=10) -> list:
    recieps_count = 0
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
        recipes = [ self.__parse_reciep(u) for u in recipes]

        # print('Saving...')
        # with open(f'data/data_{i}.json', 'w') as f:
        #   f.write(json.dumps(recipes))

        # allRecipies.extend(recipes)
      except Exception as ex:
        print(ex.args)

  def __parse_reciep(self, url) -> dict:
    try:
      resp = r.get(self.base_url + url)
      soup = BeautifulSoup(resp.text, 'lxml')
      
      res = {}
      
      description = soup.find('div', {"class": "recipe_description"})
      description = description.contents[0] if description else ""
      res["desc"] = description
      
      name = soup.find('h1', {"class": "recipe-header__name"}).contents[0]
      res["name"] = name
      
      print(f'#{recipeCount}: Creating ingredients...')
      ingredients = soup.find_all(self.__is_tag_ingredient_title)
      ingredients = [f"{i.attrs['data-intredient-title']}{self.space}{i.attrs['data-unit-id'] + i.attrs['data-unit-title']}" for i in ingredients]
      res["ingredients"] = self.newline.join(ingredients)
      
      print(f'#{recipeCount}: Creating steps...')
      steps = soup.find_all('div', {"data-module":"step_hint"})
      steps = [s.next for s in steps]
      
      res["steps"] = self.newline.join(steps)
      # print(f'#{recipeCount}: Creating tags...')
      # tags = soup.find_all(IsTagElem)
      # tags = [t.string for t in tags]

      return res
    except Exception as ex:
      print(ex.args)
      raise ex


  def __is_tag_elem(self, tag):
    return tag.attrs.get('class') and 'button' in tag.attrs.get('class') and 'button_tag' in tag.attrs.get('class')

  def __is_tag_ingredient_value(self, tag):
    return tag.attrs.get('class') and 'definition-list-table__td_value' in tag.attrs.get('class') and 'definition-list-table__td' in tag.attrs.get('class')

  def __is_tag_ingredient_title(self, tag):
    return tag.attrs.get('class') and 'checkbox__input' in tag.attrs.get('class') and 'recipe_ingredient_checkbox' in tag.attrs.get('class')

if __name__ == '__main__':
  # FindRecipes(1000)
  # with open('data/data_all.json', 'w') as f:
  #   f.write(json.dumps(allRecipies))
  s = ScrapperEdimDoma()
  res = s.scrap(s.base_words[0])
  
  print("done")