from src.shef import Shef

def main():
  print("Starting...")
  
  Shef.connect()
  number, err_number = Shef.scrap(num_pages=10,num_recipes=200)
  print(f'Recieps found {err_number + number}, added {number}({(number/(err_number + number)*100):.2f}%) recieps')
  # a = Shef.get("завтрак")
  
  print("Done")

if __name__ == "__main__":
  main()