

class Scrapper():
    
    timeout_sec:int = 1
    base_url:str = "example.com"
    base_words:list[str] = [
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
    
    def scrap(self) -> dict:
        pass