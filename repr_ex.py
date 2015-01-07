class Cat():
    def __init__(self, name, paws):
        self.name = name
        self.paws = paws

    def __repr__(self):
        return self.name

    def __repr__(self):
        return str(self.paws)

    def __repr__(self):
        return "TEMPORARY PLACEHOLDER"

    def __add__(self, other):
    	return self.paws + other.paws

my_cat = Cat("Fluffles", 4)
my_other_cat = Cat("Meowmix", 3)

print "Here's my object: %r" % my_cat
print "Here's my object: %r" % my_other_cat

print my_cat + my_other_cat



# class Cat():
#     def __init__(self, name, paws):
#         self.name = name
#         self.paws = paws

#     def __repr__(self):
#         return self.name

#     def __add__(self, other):
#         return self.paws + other.paws

# my_cat = Cat("Fluffles", 4)
# my_other_cat = Cat("Meowmix", 3)

# print "Here's my object: %r" % my_cat
# print "Here's my object: %r" % my_other_cat

# print my_cat + my_other_cat