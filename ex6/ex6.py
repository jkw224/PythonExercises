#from re import match


def try_open(f_name):

    try:
        open(f_name)
        print("You ALREADY opened the file!")
    except IOError:
        open(f_name, "w")
        print("Yay, you opened the file!")





try_open('file2')


#
# def open_file(f_name):
#     open(f_name, "w")
#
# try:
#     open_file('file')
# except IOError:
#         input("Please enter a valid file name: ")


# def validate(f_name):
#     while not match("^[a-zA-Z0-9_-]*$", f_name):
#         f_name = input("Please enter a valid filename: ")
#         continue
#
#     txt_name = f_name + ".txt"
#     create_file(txt_name)
#
#     txt_name = f_name + ".txt"
#     create_file(txt_name)
#
# unvalidated_name = input("What would you like to call your file?: ")
# validate(unvalidated_name)

