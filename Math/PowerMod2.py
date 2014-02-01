import math
def powermod(base, exponent, modulus): 
    if base < 1 or exponent < 0 or modulus < 1:
        return -1

    result = 1;
    
    while exponent > 0:
       if exponent % 2 is 1:
           result = (result * base) % modulus
       base = (base * base) % modulus
       exponent = math.floor(exponent / 2)
    
    print result