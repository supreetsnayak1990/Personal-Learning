#program to generate a grid pattern+

def vpatt(n):
    print' + - - - -'*n+' + '
def rbeam(n):
    print ' |        '*n+' | '
	
def do_twice(f,a):
    f(a)
    f(a)

def do_fourtimes(f,a):
	do_twice(f,a)
	do_twice(f,a)

def grid1(a):
    vpatt(a)
    do_fourtimes(rbeam, a)
    vpatt(a)

def grid2(a):
    do_fourtimes(rbeam, a)
    vpatt(a)
	
def finalpattern(a, b):
    grid1(a)
    count = 0
    for count in range(0,b-1):
        grid2(a)
        count = count+1

		
columns = int(raw_input("Enter the number of columns: "))
rows = int(raw_input("Enter the number of rows: "))
finalpattern(columns, rows)