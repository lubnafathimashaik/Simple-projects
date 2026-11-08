def addition(a,b):
  return a+b
def subtraction(a,b):
  return a-b
def multiplication(a,b):
  return a*b
def division(a,b):
  return a/b
def floordivision(a,b):
  return a//b
def exponent(a,b):
  return a**b
x=int(input("Enter First Number"))
y=int(input("Enter Second Number"))
c=input("Enter Operation")
if (c=='+'):
  print(addition(x,y))
elif (c=='-'):
  print(subtraction(x,y))
elif (c=='*'):
  print(multiplication(x,y))
elif (c=='/'):
  print(division(x,y))
elif (c=='//'):
  print(floordivision(x,y))
elif (c=='**'):
  print(exponent(x,y))
  
