class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog, must be in init or else it uses one list for all dogs

    def add_trick(self, trick):
        self.tricks.append(trick)
        print "Added '%s' to dog '%s'" %(trick,self.name)

jeff = Dog("Jeff")
print jeff.kind
jeff.add_trick("sit")
jeff.add_trick("lay")
print jeff.tricks
