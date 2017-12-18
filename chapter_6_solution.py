def fibonacci(n):
	if not isinstance(n,int):
		print 'Fibonacci is only defined for integers.'
		return None
	elif(n<0):
		print 'Fibonacci is not defined for negative integers.'
		return None
	elif(n==0):
		return 0
	elif(n==1):
		return 1
	else:
		return fibonacci(n-1)+fibonacci(n-2)


def fact(n):
	if not isinstance(n,int):
		print 'Factorial is only defined for integers.'
		return None
	elif(n<0):
		print 'Factorial is not defined for negative integers.'
		return None
	if(n==0):
		return 1
	else:
		return n*fact(n-1)
		
def pali(word):
	if(len(word)<=2):
		print "Length of the word is too small"
	if word == word[::-1]:
		return True
	else:
		return False
		
def pow(a,b):
	if((b%a == 0) and (pow((a/b),b))):
		return True
	else:
		return False

def gcd(a,b):
	if(b==0):
		return a
	elif(b==1):
		return 1
	else:
		return gcd(b,a%b)
		
import math
def estimate_pi():
    total = 0
    k = 0
    equation = 0
    factor = (2*math.sqrt(2))/9801
    while True:
        num = math.factorial(4*k) * (1103+(26390*k))
        den = (math.factorial(k)**4) * (396**(4*k))
        term = factor * num / den
        total += term
        k = k+1
        if (abs(term) < (1e-15)):
            break
    return 1/ total
		
		
print fact(5)
print fibonacci(4)
print pali("redivider")
print pali("Supreet")
print pow(16.0,2.0)
print gcd(15,36)
print gcd(20,13)
print estimate_pi()