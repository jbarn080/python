# The program dempostrates the use import math, exception
#	handling, assigning varaibles, modifying output, 
# 	and requesting user input
# This program is also modified to run on command line
# Initial example taken from Doing Math With Python by Amit Saha
# Modified by: James Barnhart

# defines the function roots
def roots(a, b, c):
	try:
		D = (b*b - 4*a*c)
		import math
		discrimRoot = math.sqrt(D)
		root1 = (-b + discrimRoot) / (2*a)	# modified to take variable
		root2 = (-b - discrimRoot) / (2*a)	# modified to take variable
		print('root 1: {0}'.format(root1))
		print('root 2: {0}'.format(root2))
	except ValueError:
		print("\nNo real roots found!")
		main()


# defines the main function
if __name__ == '__main__':
	a = eval(input('Enter a: '))
	b = eval(input('Enter b: '))
	c = eval(input('Enter c: '))
	roots(float(a),float(b),float(c))

# added to halt program to be run through command line
input("\nPress Enter to exit.")
