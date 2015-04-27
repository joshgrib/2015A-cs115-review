'''
CS 115 A, Spring 2015 - Test 2, Questions 7 and 8

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
' Question 7 (10 points)
' Implement this function using recursion.
' Lucas numbers follow a pattern similar to Fibonacci numbers, except that the
' first two numbers are 2 and 1. The sequence looks as follows:
' 2, 1, 3, 4, 7, 11, 18, ...
'
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def lucas(n):
    '''Returns the nth Lucas number. The 0th number is 2, the 1st number is 1,
    and any number beyond that is the sum of the previous two numbers.
    Examples:
    lucas(0) -> 2
    lucas(2) -> 3
    lucas(4) -> 7'''

    return None  # TODO replace this line with your code

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Question 8 (20 points)
' Implement this function using recursion and memoization.
' Lucas numbers follow a pattern similar to Fibonacci numbers, except that the
' first two numbers are 2 and 1. The sequence looks as follows:
' 2, 1, 3, 4, 7, 11, 18, ...
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def lucas_memo(n):
    '''Returns the nth Lucas number. The 0th number is 2, the 1st number is 1,
    and any number beyond that is the sum of the previous two numbers.
    Uses memoization to improve performance.'''

    return None  # TODO replace this line with your code


print lucas(0)  # Should be 2
print lucas(1)  # Should be 1
print lucas(2)  # Should be 3
print lucas(5)  # Should be 11
print lucas(10)  # Should be 123

print lucas_memo(0)  # Should be 2
print lucas_memo(1)  # Should be 1
print lucas_memo(2)  # Should be 3
print lucas_memo(5)  # Should be 11
print lucas_memo(10)  # Should be 123

# If you memoize correctly, these function calls will return nearly
# instantaneously.
print lucas_memo(40)  # Should be 228826127
print lucas_memo(50)  # Should be 28143753123
print lucas_memo(60)  # Should be 3461452808002