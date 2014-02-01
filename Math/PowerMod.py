def PowerMod():
  a = int(raw_input("Enter the base: "))
  n = int(raw_input("Enter the exponent: "))
  m = int(raw_input("Enter modulos: "))

  a = a%m

  b = 1 

  while n > 0:
    if (a/2)*2 is not n:
      b = (a*b)%m
      n = n-1
    else:
      a = (a*a)%m
      n = n/2
  if 2*b>m:
    b=b-m
  if 2*b < -m:
    b = b+m

  print b
