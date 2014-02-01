import math
#Testing for Prime
def is_prime(number):

    if number < 2 or number%2 is 0:
        return False
    else:
        for i in range(2,(int)(math.sqrt(number)//1)):
            if number%i == 0:
                return False
        else:
            return True
