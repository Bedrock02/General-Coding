
def inverseByFermat(a,b,mod):
	x = 1
	y = a

	while b > 0:
		if(b%2 == 1):
			x *= y
			x%=mod
		y *= y
		y%=mod
		b /= 2
	return x