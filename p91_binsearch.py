'''
CIS 210 Winter 2020
Project 9-1: Binary Search
Author: Sofia Vinas

Design, implement, and test algorithms for determining sequence inclusion
using binary search.
'''


def isMemberI(aseq, target):
    '''
    (sequence, target)-> boolean

    Takes two parameters, a sequence and a target, and determines whether or
    not the target is located in the sequence. Returns True or False.

    Examples of code:
    >>> isMemberI([1,2,3,4],4)
    True
    >>> isMemberI((),9)
    False
    '''

    for x in aseq:
        if x != int:
            pass
        else:
            aseq.sort()
    begin_index = 0
    end_index = len(aseq)-1

    while begin_index<= end_index:
        midpoint = begin_index + (end_index-begin_index) // 2
        midpoint_value = aseq[midpoint]
        if midpoint_value == target:
            return True

        elif target< midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return False

def isMemberR(aseq, target):
    '''
    (sequence, target)-> boolean

    Takes two parameters, a sequence and a target, and determines whether or
    not the target is located in the sequence. Returns True or False.

    Examples of code:
    >>> isMemberR([1,2,3,4],4)
    True
    >>> isMemberR((),9)
    False
    '''

    for x in aseq:
        if x != int:
            pass
        else:
            aseq.sort()
    
    begin_index = 0
    end_index = len(aseq)-1

    if begin_index>end_index:
        return False
    else:
        midpoint = (begin_index+end_index) // 2
        if target == aseq[midpoint]:
            return True
        elif target< aseq[midpoint]:
                return isMemberR(aseq[0:midpoint - 1], target)
        else:
            return isMemberR(aseq[midpoint +1:], target)
        

def bintest(f):
    '''
    (function)-> None

    Takes one parameter, a function, and tests for a series of test cases
    given and reports (prints) the results. Returns None.

    Examples of code:
    >>> bintest(isMemberR(aseq, target))
    Checking isMemberR((99, 100), 101)...its value False is correct!
    >>> bintest(isMemberI(aseq, target)
    Checking isMemberI((2, 10), 10)... its value True is correct!
    '''
    seq = (1,2,3,3,4)
    tar = 3
    booValue = f(seq,tar) #boolean True or False assigned to j
    functionName = str(f.__name__)
    print ('Checking ' + functionName + '('+str(seq)+','+str(tar)+')' + ' ... its value ' + str(booValue) +' is correct!')

    seq = (1,2,3,3,4)
    tar = 99
    booValue = f(seq,tar) #boolean True or False assigned to j
    functionName = str(f.__name__)
    print ('Checking ' + functionName + '('+str(seq)+','+str(tar)+')' + ' ... its value ' + str(booValue) +' is correct!')

    seq = ('aeiou')
    tar = ('i')
    booValue = f(seq,tar) #boolean True or False assigned to j
    functionName = str(f.__name__)
    print ('Checking ' + functionName + '('+str(seq)+','+str(tar)+')' + ' ... its value ' + str(booValue) +' is correct!')

    seq = ('aeiou')
    tar = 'y'
    booValue = f(seq,tar) #boolean True or False assigned to j
    functionName = str(f.__name__)
    print ('Checking ' + functionName + '('+str(seq)+','+str(tar)+')' + ' ... its value ' + str(booValue) +' is correct!')

    seq = (1,3,5,7)
    tar = 4
    booValue = f(seq,tar) #boolean True or False assigned to j
    functionName = str(f.__name__)
    print ('Checking ' + functionName + '('+str(seq)+','+str(tar)+')' + ' ... its value ' + str(booValue) +' is correct!')

    seq = (23,24,25,26,27)
    tar = 5
    booValue = f(seq,tar) #boolean True or False assigned to variable
    functionName = str(f.__name__)
    print ('Checking ' + functionName + '('+str(seq)+','+str(tar)+')' + ' ... its value ' + str(booValue) +' is correct!')

    seq = (0,1,4,5,6,8)
    tar = 4
    booValue = f(seq,tar) #boolean True or False assigned to variable
    functionName = str(f.__name__)
    print ('Checking ' + functionName + '('+str(seq)+','+str(tar)+')' + ' ... its value ' + str(booValue) +' is correct!')

    seq = (0,1,2,3,4,5,6)
    tar = 3
    booValue = f(seq,tar) #boolean True or False assigned to variable
    functionName = str(f.__name__)
    print ('Checking ' + functionName + '('+str(seq)+','+str(tar)+')' + ' ... its value ' + str(booValue) +' is correct!')

    seq = (1,3)
    tar = 1
    booValue = f(seq,tar) #boolean True or False assigned to variable
    functionName = str(f.__name__)
    print ('Checking ' + functionName + '('+str(seq)+','+str(tar)+')' + ' ... its value ' + str(booValue) +' is correct!')

    seq = (2,10)
    tar = 10
    booValue = f(seq,tar) #boolean True or False assigned to variable
    functionName = str(f.__name__)
    print ('Checking ' + functionName + '('+str(seq)+','+str(tar)+')' + ' ... its value ' + str(booValue) +' is correct!')

    seq = (99,100)
    tar = 101
    booValue = f(seq,tar) #boolean True or False assigned to variable
    functionName = str(f.__name__)
    print ('Checking ' + functionName + '('+str(seq)+','+str(tar)+')' + ' ... its value ' + str(booValue) +' is correct!')
    
    seq = (42,)
    tar = 42
    booValue = f(seq,tar) #boolean True or False assigned to variable
    functionName = str(f.__name__)
    print ('Checking ' + functionName + '('+str(seq)+','+str(tar)+')' + ' ... its value ' + str(booValue) +' is correct!')

    seq = (43,)
    tar = 44
    booValue = f(seq,tar) #boolean True or False assigned to variable
    functionName = str(f.__name__)
    print ('Checking ' + functionName + '('+str(seq)+','+str(tar)+')' + ' ... its value ' + str(booValue) +' is correct!')

    seq = ()
    tar = 99
    booValue = f(seq,tar) #boolean True or False assigned to variable
    functionName = str(f.__name__)
    print ('Checking ' + functionName + '('+str(seq)+','+str(tar)+')' + ' ... its value ' + str(booValue) +' is correct!')
    
    
def main():
    '''
    calls iterative and recursive binary search functions
    '''
    bintest(isMemberI)
    print()
    bintest(isMemberR)
    return None

main()
    
