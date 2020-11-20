#!python

def fact(n):
 if n == 0:
   return 1
 else:
   return n*fact(n-1)

num = int(input("Enter a number: "))
if num < 0:
 print ("Invalid number entered")
else:
 print ("The factorial of %d is %d" % (num,fact(int(num))))

