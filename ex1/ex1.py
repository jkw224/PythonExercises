# this function asks the user for an integer
# if the integer is a number (.isdigit) it returns their number
# to the calculate function as an int   e.g.  int(num)
def getNumber(position):
	number = input("Please enter your {} integer: ".format(position))
	if number.isdigit():
		return int(number)
	else:
		return None

# in
def calculate():
	first_int = None
	second_int = None

	while first_int is None:
		first_int = getNumber('first')

		if first_int is None:
			print("You almost fooled me! Please enter an integer...")


	zero = int(0)
	dne = "DNE"
	add = first_int + second_int
	difference = first_int - second_int
	product = first_int * second_int
	if second_int != zero:
		division = first_int / second_int
		quotient = first_int % second_int


	if second_int != zero:
		print ("The sum of %s and %s is: %s" % (first_int, second_int, add))
		print ("The difference of %s and %s is: %i" % (first_int, second_int, difference))
		print ("The product of %s and %s is: %s" % (first_int, second_int, product))
		print ("The quotient of %s and %s is %s with a remainder: %s" %\
			   (first_int, second_int, division, quotient))

	else:
		print ("\nThe sum of %d and %d is: %d" % (first_int, second_int, add))
		print ("The difference of %d and %d is: %d" % (first_int, second_int, difference))
		print ("The product of %d and %d is: %d" % (first_int, second_int, product))
		print ("The quotient of %d and %d is %s with a remainder: %s" %\
			   (first_int, second_int, dne, dne))
		print ("  **DNE means you can't divide by zero!**")

calculate()


#################
## First Edition
#################

# def calculate():
# 	int1 = input("Please enter your first integer!: ")	
# 	if int1 == int:
# 		first_int = int(int1)
# 	else:
# 		print("You almost fooled me! Please enter an integer...")


# 	int2 = input("Please enter the second interger: ")
# 	if int2 == int:
# 		second_int = int(int2)
# 	else:
# 		print("Again! Please enter an integer...")
# 		return

# 	add = first_int + second_int
# 	difference = first_int - second_int
# 	product = first_int * second_int
# 	division = first_int / second_int
# 	quotient = first_int % second_int

# 	if second_int != 0:
# 		print("The sum of " + first_int + "and " + second_int + "is: " + add)
# 		print("The difference of " + first_int + "and " + second_int + "is: " + add)
# 		print("The product of " + first_int + "and " + second_int + "is: " + add)
# 		print("The quotient of " + first_int + "and " + second_int + "is: " + \
# 		 	   division + "with a remainder: " + quotient)
# 	else:
# 		print("The sum of " + first_int + "and " + second_int + "is: " + add)
# 		print("The difference of " + first_int + "and " + second_int + "is: " + add)
# 		print("The product of " + first_int + "and " + second_int + "is: " + add)
# 		print("The quotient of " + first_int + "and " + second_int + "is: 0" + \
# 		 	   + "with a remainder: " + quotient)
