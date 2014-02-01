from CaesarCharShift import *
from BaseTwoCipher import *

def printEncoded(list):
  for code in list:
    print "%s" % code,

def CBE():
  message = raw_input("Enter your message to encrypt. Letters should be in all CAPS: ")
  shift = int(raw_input("What is the key you wish to encrypt with: "))
  messageList = message.split()
  resultList = []
  resultWord = ''
    
  for word in messageList:
    for i in word:
		resultWord = resultWord + CaesarCharShift(i,shift)
    resultList.append(resultWord)
    resultWord = ''

  printEncoded(BaseTwoCipher(resultList))  
  
if __name__ == '__main__':
  CBE()