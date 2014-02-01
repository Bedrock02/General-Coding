#this algorithm finds one factor of a given number
from gcd import *
def f(x):
	return (x*x+1)

def Rho(n):
	fList = [f(2)]
	i = 2
	while(i<n):
		fList.append(f(fList[-1]))
		factor = gcd(fList	[(2*(i/2))-1]-fList[(i/2)-1],n)
		if(i%2==0 and factor > 1):
			return factor
		i=i+1