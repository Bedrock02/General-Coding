from DecimalToBinary import *
def BaseTwoCipher(messageList):
	'''message will be a string of characters
		1.convert the string into characters do not have spaces
		2.convert each character into an integer
		3.Display in a binary
	'''
	BinaryList = []
	for i in messageList:
		for x in i:
			BinaryList.append(decimalToBinary(ord(x)))
	return BinaryList