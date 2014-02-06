#program collects the primes from 1 to 1009 from primes .txt file returns a collection of primes
def primeCollection():
	primes = []
	f = open('primes.txt','r')
	lines = f.readlines()

	for line in lines:
		sublist = map(lambda s: int(s), line.strip().split(" "))
		primes += sublist
	
	return primes
primes = primeCollection()
