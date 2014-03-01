# n = pq, pq are consecutive primes

import math
from primeTest import *
def findPrimeFactor(number):
	if is_prime(number):
		print "This number is prime!"
		return

	m = int(math.sqrt(number))
	while True:
		m += 1
		y = math.sqrt(pow(m,2)-number)
		if int(y) == y:
			y = int(y)
			break

	b = m - y 
	a = m*2 - b
	return (b,a)

