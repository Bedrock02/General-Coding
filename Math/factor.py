from pollardRho import *
from primeCollection import *
from collections import defaultdict
import math

def factor(number):
	#list of primes from 1 to 1009
	collection = primeCollection()
	
	#Hash that will hold the factors of a number
	factors = defaultdict(int)
	#for all the primes in the list
	for prime in collection:
		
		#don't check any primes greater than number
		if prime > number:
			break
		
		#count how many times this prime can go into the number		
		while number%prime == 0:
			factors[prime] += 1
			number/=prime 

	return factors




