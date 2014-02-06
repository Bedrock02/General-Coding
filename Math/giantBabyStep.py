#This is the Giant step Baby Step Algorithm
#What is needed for this function is a prime number a primiitve root and the goal number

import math

def giantBabyStep(prime,primitiveRoot,goalNumber):
  
	#Calculate m
  m = int(math.ceil(math.sqrt(prime-1)))
  #a = i*m + j
  #goalNumber = primitiveRoot^a (mod prime) = goalNumber^(i*m+j) (mod prime)
  # then g^j = xg^-im (mod prime)
  
  #Store all the giant steps taken
  giantSteps = {}
  for i in xrange(0,m):
  	giantSteps[int(goalNumber*(primitiveRoot**(-i*m))%prime)] = i
  
  #Find the babysteph that matches the giant steps taken
  j=0
  while(True):
  	babyStep = (primitiveRoot**j)%prime
  	
  	#If a match is found then use the i and j found
  	if babyStep in giantSteps:
  		print "X is of value %s" % (giantSteps[babyStep]*m + j)
  		return
  	j += 1

if __name__ == '__main__':
	print "The Giant Step Baby Step Algorith solves for x in the following:"
	print "p being a prime number,g being a primitive root mod p, and t being a number between 1 and p (excluding p)"
	print " g^x = t mod p"
	prime = int(raw_input("Enter the prime number "))
	primitiveRoot = int(raw_input("Enter the primitive root "))
	goalNumber = int(raw_input("Enter your value of t or the target number "))
	giantBabyStep(prime,primitiveRoot,goalNumber)
