#this algorithm finds one factor of a given number
from gcd import *
def f(x,n):
	return (pow(x,2,n)+1)%n
def Rho(n):	
	factors = {}
	i = 1
	x = 1
	d = 1
	
	while d == 1:
		#Calculate x[i]
		factors[i] = f(x,n)
		#Calculate x[i+1]
		factors[i+1] = f(factors[i],n)
		
		#find the gcd
		d = gcd(abs(factors[(i+1)/2] - factors[i+1]),n)

		#if not relatively prime return d
		if d > 1:
			return d
		#continue iteration
		else:
			x = factors[i+1]
			i+=2
