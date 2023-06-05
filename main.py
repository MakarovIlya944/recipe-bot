from src.shef import Shef

def main():
  print("Starting...")
  
  s = Shef()
  s.connect()
  number, err_number = s.scrap()
  print(f'Recieps found {err_number + number}, added {number}({(number/(err_number + number)*100):.2f}%) recieps')
  print("Done")

if __name__ == "__main__":
  main()