# Function to gather user input
def get_user_input(input_value):
    user_input = input("Please enter " + input_value + " integer: ")

    while True:
        try:
            # Check user input for int
            int(user_input)
            # Check user input for 0 is it is the second number
            if input_value is "second":
                1 / int(user_input)
        except ValueError:
            user_input = input("Integers only please, enter " + input_value + " number: ")
            continue
        except ZeroDivisionError:
            user_input = input("We are dividing, so no zeros, enter  " + input_value + "  number: ")
            continue
        else:
            break

    return user_input


# User input variables
inputs = ['first', 'second']
num_one = int(get_user_input(inputs[0]))
num_two = int(get_user_input(inputs[1]))

#Output
print("Sum of %i and %i is: %i" % (num_one, num_two, (num_one + num_two)))
print("The difference of %i and %i: %i" % (num_one, num_two,  (num_one - num_two)))
print("The product of %i and %i is: %i" % (num_one, num_two, (num_two * num_one)))
print("The quotient of %i and %i: %i with remainder: %i" % (num_one, num_two, num_two, (num_one % num_two)))