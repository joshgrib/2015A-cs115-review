'''
CS 115 A, Spring 2015 - Test 3, Questions 7 and 8

Author: <your name here>
Pledge: <write pledge>
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' RULES: You can use Canvas to download this file and upload your solution.
' You can use Eclipse to edit and run your program. You should NOT look at
' other programs in Eclipse, you should NOT use any other programs, and you
' should NOT use any notes or books.
' According to the Honor Code, you should report any student who appears
' to be violating these rules.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Question 7 (20 points)
' Implement the missing sections of the Star class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import math
from random import randint

class Star(object):

    def __init__(self, x, y):
        '''Initializes the PRIVATE fields x and y with the values received as
        arguments. You may assume x and y are valid integers.'''
        pass  # TODO replace this line with your code

    # Write properties for x and y here.

    # Write the method that checks if this Star is equal to another Star here.
    # Two Stars are equal if their x and y coordinates are equal. Be sure
    # to overload the correct operator for use with ==.

    def distance_to(self, other):
        '''Computes the distance to the other Star passed as an argument to
        the method.
        Recall the distance formula (not written in valid Python syntax):
        d = sqrt( (x2 - x1)^2 + (y2 - y1)^2 )
        '''
        return None  # TODO replace this line with your code

    def __str__(self):
        '''Returns the string representation of the location of the Star, such
        as (3, 2) or (-1, 5). Note the space after the comma.'''
        return None  # TODO replace this line with your code

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Question 8 (10 points)
' Implement the missing sections of the Sky class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Sky(object):

    def __init__(self):
        '''Initializes the Sky object with between 5-10 Stars randomly
        generated.'''
        self.__stars = []
        for _ in range(randint(5, 10)):
            self.__stars.append(Star(randint(-100, 100), randint(-100, 100)))

    def westernmost_star(self):
        '''Returns the westernmost Star in the Sky (Star with the lowest x
        value).'''
        return None  # TODO replace this line with your code

    def northernmost_star(self):
        '''Returns the northernmost Star in the Sky (Star with the highest y
        value).'''
        return None  # TODO replace this line with your code

    def __str__(self):
        '''Returns a string representation of the list of coordinates of the
        Stars in the Sky.'''
        return '[' + ', '.join(map(str, self.__stars)) + ']'

if __name__ == '__main__':
    print Star(1, 2) == Star(1, 2)
    print Star(1, 2) == Star(2, 1)
    sky = Sky()
    w = sky.westernmost_star()
    n = sky.northernmost_star()
    print 'Stars in sky:', sky
    print
    print 'Westernmost star:', w
    print 'Northernmost star:', n
    print 'Distance:', w.distance_to(n)