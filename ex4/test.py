user_input = "hi"

with open("ex4_user_input_file", 'a') as file:
    file.write(user_input)

print("Your file now reads: " + file)