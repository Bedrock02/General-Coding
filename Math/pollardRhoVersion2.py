import gcd import *
def f(x):
	return (x*x+1)
def Rho(n):
	fList = [f(2)]
	for i in xrange(2,n):
		fList.append(f(fList[-1]))
		factor = gcd(fList	[(2*(i/2))-1]-fList[(i/2)-1],n)
		if(i%2==0 and factor > 1):
			print "This is a factor ",factor
			break

	print n/factor
