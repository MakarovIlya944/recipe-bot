from src.scrappers.edimdoma import ScrapperEdimDoma

def main():
  print("Starting...")
  scrapper_edimdoma = ScrapperEdimDoma()
  
  res = scrapper_edimdoma.scrap("завтрак")
  
  print("Done")

if __name__ == "__main__":
  main()