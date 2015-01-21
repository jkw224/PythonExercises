class Person:
    def __init__(self, name="", age=0, birthdate="", address=""):
        self.name = name
        self.age = age
        self.birthdate = birthdate
        self.address = address

    def __str__(self):
        name_str = "Person Name: " + self.name + "\n"
        age_str = "Person Age: " + str(self.age) + "\n"
        birthday_str = "Person Birthday: " + self.birthdate + "\n"
        address_str = "Person Address: " + self.address + "\n"

        final_str = name_str + age_str + birthday_str + address_str

        return final_str

chris = Person('Chris', 25, '12/1/1990', '123 Steet')
linsey = Person('Chris', 25, '12/1/1990', '567 Steet')
no_one = Person()

print(chris)
print(linsey)
print(no_one)