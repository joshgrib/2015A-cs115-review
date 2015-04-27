'''
Created on Apr 15, 2015
@author: Brian Borowski

CS115 - Exceptions
'''
import sys

def my_divide(x, y):
    if y == 0:
        raise ZeroDivisionError('Cannot divide ' + str(x) + ' by 0.')
    return x / y

if __name__ == '__main__':
    str_value = raw_input('Enter an integer: ')
    try:
        int_value = int(str_value)
    except:
        # Type of error not specified, so just handle when a string
        # cannot be converted to int. Technically, this is a TypeError.
        print 'Error: Please be sure to enter an integer.'
        sys.exit(1)  # Program terminated with an error.
    print 'You entered', int_value

    try:
        print my_divide(int_value, 0)
    except ZeroDivisionError as error:
        print 'Error:', error
        sys.exit(1)  # Program terminated with an error.
    sys.exit(0)  # Program terminated successfully.
