'''
Created on Apr 13, 2015
@author: Brian Borowski

CS115 - Functions that merge lists
'''
def num_matches(list1, list2):
    '''Returns the number of elements that the two lists have in common.'''
    list1.sort()
    list2.sort()
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def keep_matches(list1, list2):
    '''Returns a list of the elements that the two lists have in common.'''
    list1.sort()
    list2.sort()
    result = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return result

def drop_matches(list1, list2):
    '''Returns a new list that contains only the elements in list2 that are NOT
    in list1.'''
    list1.sort()
    list2.sort()
    result = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            result.append(list2[j])
            j += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1
    return result

if __name__ == '__main__':
    A = [2, 3, 5, 7, 9, 11, 13, 17, 23]
    B = [11, 13, 15, 17, 19, 21, 23, 25, 27]
    C = keep_matches(A, B)
    print C
    C = drop_matches(A, B)
    print C