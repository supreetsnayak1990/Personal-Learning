def is_triangle(a,b,c):
	if(a>b+c):
		print"No"
	elif(b>a+c):
		print"No"
	elif(c>a+b):
		print"No"
	else:
		print"Yes"
		
def check_is_triangle():
	a = int(raw_input("Enter the first side: "))
	b = int(raw_input("Enter the second side: "))
	c = int(raw_input("Enter the third side: "))
	is_triangle(a,b,c)

check_is_triangle()