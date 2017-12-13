def check_fermat(a,b,c,n):
	if ((a**n)+(b**n)==(c**n)):
		print"Holy Smokes, Fermat is wrong!!"
	else:
		print"No this does not work"


def check_fermat_user():
	a = int(raw_input("Enter the first number: "))
	b = int(raw_input("Enter the second number: "))
	c = int(raw_input("Enter the third number: "))
	n = int(raw_input("Enter the power (greater than 2): "))
	check_fermat(a,b,c,n)

check_fermat_user()