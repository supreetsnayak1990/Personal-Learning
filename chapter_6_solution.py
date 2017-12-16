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

		
print fact(5)
print fibonacci(4)
print pali("redivider")
print pali("Supreet")