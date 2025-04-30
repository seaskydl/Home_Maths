from cnocr import CnOcr
ocr = CnOcr()

def welcome():
  print("Welcome to Home Maths Helper")

def readPic():
  print("Step 1: Read Pic")

def identifyPic():
  print("Step 2: Identify Pic")
  file_name = "./data/huochepiao.jpeg"
  result = ocr.ocr(file_name)
  print("result:", result)

def verify():
  print("Step 3: Verify")

def doHomework():
  readPic()
  identifyPic()
  verify()

def main():
  welcome()
  doHomework()

if __name__ == "__main__":
  main()