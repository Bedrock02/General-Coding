def decimalToBinary(decimal):
	if decimal is 1:
		return '1'
	return decimalToBinary(decimal/2) + str(decimal%2)