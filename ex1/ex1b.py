def get_number(position):
	number = input("Enter your {} interger!").format(position))
	if number.isdigit():
		return int(number)
	else:
		return None


def user_input():
	first_int = None
	second_int = None

	while first_int is None:
		first_int = get_number('first')

		if first_int is None:
			print("Enter an number!")

	while second_int is None:
		second_int = get_numbers('second')	

		if second_int is None:
			print("You know the drill! Enter an integer!")

	return (first_int, second_int)


def calculate():
	first_int, second_int = user_input()

	zero = int(0)
	add = first_int + second_int
	difference = first_int - second_int
	if second_int is not zero
		division = first_int / second_int
		quotient = first_int % second_int


def display():
	dne = "DNE"
	zero = int(0)
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