#this function tests if a number is a primitive root mod m 
from factor import *
def is_primiitve(number,mod):
	factorsOfToitent = factor(mod-1)
	for prime in factorsOfToitent:
		for exp in xrange(1,factorsOfToitent[prime]+1):
		  if prime**exp == mod-1:
		  	return True
		  if number**(prime**exp)%mod == 1:
		  	return False
	return True
	
print is_primiitve(5,65537)
