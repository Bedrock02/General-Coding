#Make sure that Rational(2) is Rational(4,2)
#include Zero Divison Error
from gcd import *
def reduce(x,y):
  d = gcd(x,y)
  return (x/d,y/d)



class Rational(object):
  instances = {}
  __slots__ = "num","den"

  def __new__(cls,x,y):
    
    tup = reduce(x,y)
    #reduce must be done here or else it will not work
    if tup not in cls.instances:
      new = object.__new__(cls)
      new.num = tup[0]
      new.den = tup[1]
      cls.instances[tup] = new
    return cls.instances[tup]

  def __str__(self):
    if self.num is 0:
      return "0"
    if self.den is 1:
      return str(self.num)
    return "%s / %s" % (self.num,self.den)

  __repr__=__str__

  #MULTIPLICATION
  def __mul__(self,other):
    if type(other) is Rational:
      return Rational(self.num*other.num,self.den*other.den)
  
    if type(other) in [int,float]:
      return self.__mul__(Rational(other))
  
  def __rmul__(self,other):
    return self.__mul__(other)


 #ADDITION
  def __add__(self,other):
    if type(other) is Rational:
      print Rational((self.num*other.den)+(other.num*self.den),(other.den*self.den))
    
    if type(other) in [int,float]:
    	return self.__add__(Rational(other))

  def __radd__(self,other):
    return self.__add__(other)

  #SUBTRACTION
  def __sub__(self,other):
    if type(other) is Rational:
      print Rational((self.num*other.den)+ -(other.num*self.den),(other.den*self.den))
    
    if type(other) in [int,float]:
      return self.__sub__(Rational(other))
  
  #DIVISION
  def __div__(self,other):
    if type(other) is Rational:
      return Rational(self.num*other.den,self.den*other.num)

    if type(other) in [int,float]:
      return self.__div__(Rational(other))
      
  
  def __neg__(self):
    return Rational(-self.num,self.den)
    
  
  def __invert__(self):
    if self.num<0:
      return Rational(-self.den,-self.num)       
    return Rational(self.den,self.num)
  
  __iadd__=__add__

  __imul__=__mul__
  
  __idiv__=__div__
  
  def __pow__(self,other):
    return Rational(self.num **other,self.den**other)
  
  __ipow__=__pow__

  
  def __cmp__(self,other):
    if self.den is other.den:
      return cmp(self.num,other.num)
    return cmp(self.num*other.den,other.num*self.den)    

Rational(1,2)
print Rational(1,2) is Rational(1,2)