def main():
    print("***************************\n EXERCISE 4 - MENU\n***************************\n")
    print("1. Write input to file\n2. Write input to screen\n3. Quit\n")
    user_choice = input("***************************\nEnter your choice [1-3] : ")

    if user_choice is not isinstance(user_choice, int):
        user_response = input_checker(user_choice)

    user_input = input("Enter a input: ")

    if user_response == str(1):
        # write data to a file
        file = open("ex4_user_input_file", 'a')
        file.append(user_input)
        print("Your file now reads: " + file)
    elif user_response == str(2):
        # print data to screen
        print("Printing your input...\n" + user_input)
    else:
        # Quit
        print("Quitting program...")
        print("fin")



def input_checker(user_response):
    while True:
        if isinstance(user_response, str):
            user_response = input("**Error** Need to enter a number: ")
            continue
        elif isinstance(user_response, float):
            user_response = input("**Error** Enter a non-decimal number: ")
            continue
        else:
            break

    return user_response


main()