
class Scrapper():
    
    timeout_sec:float = 0.5
    base_url:str = "example.com"
    base_words = [
        "завтрак",
        "обед",
        "ужин",
        "закуска",
        "салат",
        "суп",
        "горячее",
        "десерт",
        "выпечка",
        "напитки",
        ]
    
    newline:str = "\n"
    space:str = " "
    
    def __init__(self) -> None:
        pass
    
    def scrap(self, base_word: str, with_ingredient: str=None, without_ingredient: str=None) -> list:
        pass