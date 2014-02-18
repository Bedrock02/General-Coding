#DLP by brute force
def dlpBruteForce(prime,primitiveRoot,target):
	for i in xrange(1,prime):
		if (primitiveRoot**i)%prime == target:
			print "Found: %s" % (i)
			break
	
if __name__ == '__main__':
	print "The Giant Step Baby Step Algorith solves for x in the following:"
	print "p being a prime number,g being a primitive root mod p, and t being a number between 1 and p (excluding p)"
	print " g^x = t mod p"
	prime = int(raw_input("Enter the prime number "))
	primitiveRoot = int(raw_input("Enter the primitive root "))
	goalNumber = int(raw_input("Enter your value of t or the target number "))
	dlpBruteForce(prime,primitiveRoot,goalNumber)	
