# The program dempostrates the use from math import sqrt
#	assigning varaibles, modifying output, and requesting
# 	user input
# This program is also modified to run on command line
# Initial example taken from Doing Math With Python by Amit Saha
# Modified by: James Barnhart

# defines the function roots
def roots(a, b ,c):
	from math import sqrt			# modified to import sqrt from math
	discrim = sqrt(b*b - 4*a*c)		# variable assigned with sqrt
	root1 = (-b + discrim) / (2*a)	# modified to take variable
	root2 = (-b - discrim) / (2*a)	# modified to take variable

	print('root 1: {0}'.format(root1))
	print('root 2: {0}'.format(root2))

# defines the main function
if __name__ == '__main__':
	a = input('Enter a: ')
	b = input('Enter b: ')
	c = input('Enter c: ')
	roots(float(a),float(b),float(c))

# added to halt program to be run through command line
input("\nPress Enter to exit.")
