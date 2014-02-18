#This is the Giant step Baby Step Algorithm
#What is needed for this function is a prime number a primiitve root and the goal number

import math
from inverse import*

def babyGiantStep(prime,primitiveRoot,goalNumber):
  

  m = int(math.ceil(math.sqrt(prime-1)))
  
  giantSteps = {}
  for j in xrange(0,m):
    giantSteps[pow(primitiveRoot,j,prime)] = j
    
  #find inverse of generator
  inverse = inverseByFermat(primitiveRoot,prime-2,prime)
  inverseToM = pow(inverse,m,prime)

  suspect = goalNumber

  for i in xrange(0,m):
    if suspect in giantSteps:
      return i * m + giantSteps[suspect]
    else:
      suspect = suspect * inverseToM % prime
  print "nothing"

if __name__ == '__main__':
	print "The Giant Step Baby Step Algorith solves for x in the following:"
	print "p being a prime number,g being a primitive root mod p, and t being a number between 1 and p (excluding p)"
	print " g^x = t mod p"
	prime = int(raw_input("Enter the prime number "))
	primitiveRoot = int(raw_input("Enter the primitive root "))
	goalNumber = int(raw_input("Enter your value of t or the target number "))
	babyGiantStep(prime,primitiveRoot,goalNumber)
