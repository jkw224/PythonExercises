# how to write a good exception wo
import re

def main():
    print("***************************\n EXERCISE 4 - MENU\n***************************\n")
    print("1. Write input to file\n2. Write input to screen\n3. Quit\n")
    user_choice = input("***************************\nEnter your choice [1-3] : ")

    # only prompt for input if user enters 1 or 2
    if user_choice == ("1" or "2"):
        user_input = input("Enter a phrase: ")

    # if user enters 1, prompt for filename to write to
    if user_choice == ("1"):
        name_of_file = input("What would you like to name your file? ")

        # Using regular expression to make sure, the filename has valid characters
        while not re.match("^[a-zA-Z0-9_]*$", name_of_file):
            name_of_file = input("Unsupported filename character. Please enter another filename: ")

        # Append .txt to filename
        file = name_of_file + ".txt"


    # Output to user input 1, 2, or 3
    if user_choice is "1":
        # write data to a file
        with open(file, "a+") as new_file:
            new_file.write(user_input)
        with open(file, "r") as f:
            for line in f:
                print(line)
    elif user_choice == str(2):
        # print data to screen
        print("Printing your input...\n" + user_input)
    elif user_choice == "3":
        # Quit
        print("Quitting program...")
        print("fin")
    else:
        print("Please enter 1, 2, or 3")


main()