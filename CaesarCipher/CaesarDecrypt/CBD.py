from BinarytoCharacter import BinaryToChar
from CaesarCharShiftDecoder import CaesarCharShiftDecoder

def CBD():

  cipherText = raw_input("Enter the encoded binary sentance. Binary numbers should be separated with a space ") 
  cipherKey = int(raw_input("What is the key?"))
  
  cipherText2 = BinaryToChar(cipherText)
  for i in cipherText2:
    print CaesarCharShiftDecoder(i,cipherKey),

if __name__ == '__main__':
	CBD()