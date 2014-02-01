def BinaryToChar(message):
  result = ''
  cipherList = message.split()
  for i in cipherList:
		result = result + chr(int(i,2))
  return result