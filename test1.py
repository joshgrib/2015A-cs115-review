'''Question 8'''
def keep_excitement_fil(lst):
    return filter((lambda x: x[-1] == '!'), lst)
myList = ['dog','dog!','cats','cats!']
print keep_excitement_fil(myList)
#>>>['dog!', 'cats!']
