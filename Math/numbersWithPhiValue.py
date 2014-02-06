from Phi import *
def numbersWithPhiValue(number,maxSearchNumber):
	answer = []
	
	for i in xrange (1, maxSearchNumber):
		phiValue = len(PhiFunc(i))
		
		if phiValue == number and phiValue not in answer:
			answer.append(i)

	return answer



