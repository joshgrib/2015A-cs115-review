# Josh Gribbon
# Notes sheet for CS115 final
'''RECURSION, RANGE'''


def reduce_rec(lst):
    if lst == []:
        return 0
    else:
        return lst[0] + reduce_rec(lst[1:])
print reduce_rec(range(4))
#>>6
'''FILTER, LAMBDA'''


def keep_excitement_fil(lst):
    return filter((lambda x: x[-1] == '!'), lst)
myList = ['dog', 'dog!', 'cats', 'cats!']
print keep_excitement_fil(myList)
#>>>['dog!', 'cats!']
'''MAP, LAMBDA, RANGE'''
deezSquares = map((lambda x: x ** 2), range(0, 10, 2))
print deezSquares
#>>>[0, 4, 16, 36, 64]
'''REDUCE, LAMBDA'''
deezReducedSquares = reduce((lambda x, y: x + y), deezSquares)
print deezReducedSquares
#>>>120
'''CLASSES'''


class Animal:  # show some inheritance just in case I need to show it

    def __init__():
        pass  # maybe put weight, age, and some other stuff here


class Dog(Animal):
    type = 'canine'  # shared by all instances of "Dog"

    def __init__(self, name, weight, age):
        self.__name = name
        self.__tricks = []    # creates a new empty list for each dog
        self.__weight = weight
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        '''Used to let the value be set/updated later'''
        local_age = 0
        try:
            local_age = int(age)
        except:
            raise TypeError("Age must be an integer")
        if local_age < 0:
            raise ValueError('Age must be at least 0')
        self.__age = local_age

    def __str__(self):
        return str(self.__name) + ': weight-' + str(self.__weight) + ', age-' + str(self.__age) + ', tricks:' + str(self.__tricks)

    def __repr__(self):
        return "<Dog {'name':'" + str(self.__name) + "', 'weight':" + str(self.__weight) + ", 'age':" + str(self.__age) + ", 'tricks':" + str(self.__tricks) + "}>"

    def add_trick(self, trick):
        self.tricks.append(trick)
fido = Dog('Fido', 75, 4)
print fido
#>>>Fido: weight-75, age-4, tricks:[]
print fido.weight
#>>>75
print repr(fido)
#>>><Dog {'name':'Fido', 'weight':75, 'age':4, 'tricks':[]}>
'''MEMOIZATION'''


def lucas(n):
    '''Returns the nth Lucas number. The 0th number is 2, the 1st number is 1,and any number beyond that is the sum of the previous two numbers. Examples:lucas(0) -> 2 lucas(2) -> 3 lucas(4) -> 7'''
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)


def lucas_memo(n):
    '''Returns the nth Lucas number. The 0th number is 2, the 1st number is 1,and any number beyond that is the sum of the previous two numbers. Uses memoization to improve performance.'''
    def lucas_helper(n, memo):
        if n in memo:
            return memo[n]

        if n == 0:
            result = 2
        elif n == 1:
            result = 1
        else:
            result = lucas_helper(n - 1, memo) + lucas_helper(n - 2, memo)

        memo[n] = result
        return result

    return lucas_helper(n, {})
'''DEEP VS SHALLOW COPY'''
# a change in a nested object will change all references to it
import copy
lst1 = ['a', 'b', ['c', 'd']]
lst2 = lst1
lst3 = copy.deepcopy(lst1)
lst1[2][0] = 'x'
print lst2
#>>>['a', 'b', ['x', 'd']]
print lst3
#>>>['a', 'b', ['c', 'd']]
'''USE IT OR LOSE IT'''


def packBag(capacity, items):
    '''Takes items to get as close as possible without going over capacity'''
    if capacity <= 0 or items == []:
        return 0
    elif items[0] > capacity:
        return packBag(capacity, items[1:])
    else:
        loseIt = packBag(capacity, items[1:])
        useIt = items[0] + packBag(capacity - items[0], items[1:])
        return max(loseIt, useIt)
print packBag(20, [1, 2, 5, 10, 6])
#>>>19
# Using 1,2,10,and 6


def tSum(target, L):
    '''Determines whether or not it is possible to create target sum using the values in the list.'''
    if target == 0:
        return True
    if L == []:
        return False
    use_it = tSum(target - L[0], L[1:])
    lose_it = tSum(target, L[1:])
    return use_it or lose_it
print tSum(20, [10, 4, 2, 7, 11, 1])
#>>>True
print tSum(20, [10, 4, 4, 7, 1])
#>>>False
'''ERROR HANDLING'''
try:
    print "4" + 20
except TypeError as error:
    print error
    print "You cannot blaze it with strings and ints"
#>>>cannot concatenate 'str' and 'int' objects
#>>>You can't blaze it with strings and ints"
if (deezReducedSquares > 800):
    raise UserWarning("Too hot, hot damn")
'''UNIT TESTING'''
import unittest
class MyTests(unittest.TestCase):
    #Only functions starting with "test" get tested
    def test1(self):
        self.assertEqual(2 + 2, 4)
    def test2(self):
        self.assertTrue(2 == 2)
        self.assertFalse(2 == 3)
    def test3(self):
        with self.assertRaises(TypeError):
            spam = 2 + "eggs"
if __name__ == '__main__':
    unittest.main() #nothing after this in the file runs
#>>>...
#>>>----------------------------------------------------------------------
#>>>Ran 3 tests in 0.000s
#>>>
#>>>OK
'''SYS.EXIT()'''
import sys
#sys.exit("Time to exit")
#>>>I'm out
# sys.exit(0) #clean "proper" exit
# sys.exit(1) #exit because of a problem
'''BOX AND ARROW DIAGRAMS'''
# http://www.cs.hmc.edu/csforall/_images/fivepointtwo.png

#=============================================================================================================#


'''TWOS COMPLEMENT'''
# Show -28 in 8-bit binary
# First write 28
00011100
# Flip every value
11100011
# Add 1
11100100
# http://stackoverflow.com/questions/1049722/what-is-2s-complement
# if it starts with a 0 its positive, if it starts with a 1 its negative
'''USE IT OR LOSE IT'''
# http://www.cs.hmc.edu/csforall/FunctionalProgramming/functionalprogramming.html#use-it-or-lose-it
# https://www.youtube.com/watch?v=H_RpnvKq4dM
# This is something that seems solely from HMC
# This works when you need to make a decision to continue along your path
# of give up on it and try a different one. You make two recursive calls,
# one on your path "useIt" and one on the other path "loseIt". Then within
# each of those it happens again. Then once the base case is met the
# function tells its call which path was better, back up the chain and
# giving the total result to the first call

'''BOOLEAN LOGIC NOTATION'''
# and or not nand nor xor

#=============================================================================================================#


# http://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
# https://docs.python.org/2/tutorial/classes.html
# wiki.python.org/moin/SimplePrograms

'''Topics covered on test 2
    Recursion (may need lambda)
    Use it or lose it
    Dictionaries
    Memoization (with and without returning the values of a solution, as in knapsack, LCS, subset sum)
    Circuits
    Number bases, twos complement, mathematical operations in binary
    Unit testing with PyUnit
'''
'''Topics covered on test 3
    References (deep vs. shallow copy) and box-and-arrow diagrams.  See Game of Life lab for review.
        http://www.cs.hmc.edu/csforall/_images/fivepointtwo.png
    Tracing and writing loops (for and while, and of course, details of range())
    Exceptions:
        try/except/raise
        ValueError
        TypeError
        ZeroDivisionError
    2D lists.  See example from class on printing the 2D board and how we looped over the rows and columns.
    Classes:
        Constructor (__init__)
        Properties
        Setters
            https://sit.instructure.com/courses/3333/files/624546?module_item_id=166199
        __str__
        __repr__
        operator overloading __eq__, __lt__, __gt__, etc.  (See Fraction class)
            https://sit.instructure.com/courses/3333/files/593437?module_item_id=163082
'''
'''Other things I saw
 ** File I/O
'''


class Person(object):

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def __str__(self):
        return self.__first_name + " " + self.__last_name


class Student(Person):

    def __init__(self, first_name, last_name, gpa):
        Person.__init__(self, first_name, last_name)
        self.__gpa = gpa

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, gpa):
        local_gpa = 0
        try:
            local_gpa = float(gpa)
        except:
            raise TypeError("GPA must be a float")
        if 4.0 < local_gpa < 0:
            raise ValueError('GPA must be between 0 and 4')
        self.__gpa = local_gpa

    def __str__(self):
        return Person.__str__(self) + " has a gpa of " + str(self.__gpa)
s = Student('John', 'Doe', 3.7)
s.gpa = 3.9
print s
#>>>John Smith has a gpa of 3.9


'''
class Person:
    def __init__(self , first , last ):
        self.firstName = first
        self.lastName = last
    def asleep(self , time ):
        return 0 <= time <= 7
    def __str__(self ):
        return self.firstName + " " + self.lastName
class Student(Person ):
    def __init__(self , first , last , gpa):
        Person.__init__(self , first , last)
        self.gpa = gpa
    def asleep(self , time ):
        return 3 <= time <= 11
    def __str__(self ):
        return Person.__str__(self) + ", " + str(self.age) \
         + " GPA=" + str(gpa)
class StevensStudent(Student ):
    def __init__(self , first , last , gpa):
        Student.__init__(self , first , last , gpa)
    def __str__(self ):
        return Person.__str__(self)
    def status(self , time ):
        if self.asleep(time ):
            return str(self) + " is asleep now."
        return str(self) + " is studying or thinking about studying."
a = StevensStudent ("Steven", "Gabarro", 3.9)
b = StevensStudent ("Brian", "Borowski", 1.0)
c = StevensStudent ("Dave", "Naumann", 1.0)
print a.status (10)
#>>>Steven Gabarro is asleep now.
'''
