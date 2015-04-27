'''
Created on Jan 27, 2015

@author: Brian Borowski

CS115 - Functions returning functions
'''

def div(k):
    '''Checks whether 42 is evenly divisible by an integer k.'''
    return 42 % k == 0

def divides(n):  # What does this do?
    def div(k):
        return n % k == 0
    return div

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def increment(k):
    '''Returns a function that adds k to a number.'''
    return None

def inc_all(nums, n):
    '''Add n to every number in a given list of numbers.'''
    return None

def test_inc_all():
    '''Tests for inc_all. Correct tests print True.'''
    print inc_all([], 2) == []
    print inc_all([1, 3, 5], 2) == [3, 5, 7]
    print inc_all([-2, -1, 0, 1, 2], 10) == [8, 9, 10, 11, 12]

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Another example involving functions that return functions.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
words = ['abate', 'abbey', 'abet', 'abhor', 'abide', 'able', 'ably',
         'about', 'above', 'abundant', 'abuse', 'abyss', 'ac', 'ace',
         'ache', 'achy', 'acid', 'acne', 'acorn', 'acre', 'acrid']

def make_len(n):
    '''Assume n is a non-negative integer. Return a function.
    That function applies to strings. It concatenates * characters
    to the given string, to make its length at least n.'''
    def pad_it(word):
        return None  # TODO
    return pad_it

def pad(words):
    '''Assume words is a non-empty list of strings. Let n be the
    length of the longest. Return a list of the same strings except
    with enough * characters appended to make each one length n.'''
    return None  # TODO

def test_pad():
    '''Tests for pad. Correct tests print True.'''
    print pad(['abate', 'abbey']) == ['abate', 'abbey']  # no padding
    print pad(['a', 'cat']) == ['a**', 'cat']
    print pad(['three', 'cats', 'asleep', 'now']) \
           == ['three*', 'cats**', 'asleep', 'now***']

test_inc_all()
test_pad()