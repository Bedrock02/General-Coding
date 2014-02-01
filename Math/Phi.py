from gcd import *

def PhiFunc(n):
	Philist = []
	for i in xrange(1,n):
	  if(gcd(n,i)==1):
	  	Philist.append(i)
	return Philist