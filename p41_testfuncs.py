'''
CIS 210 W20 Project 4-1: Testing

Author: Sofia Vinas

Credits: N/A


This week's project focuses on creating and implementing your own
functions to automate testing.
'''

import p34_sscount_key as p34

def test_sscount(f, args, expected_result):
    '''
    (function, string, int)-> None

    This function takes three parameters. The first paramenter is f, a function
    will be sscount0 or sscount1. The second argument is args, a string with the
    "needle" and the "haystack" strings, separated by one space character. The
    final argument is expected_result, an integer which is the expected result of
    calling one of the sscount functions for the needle and haystack strings
    in args. test_sscount will call f for the needle and haystack string in args,
    and compare the result returned by f to the expected result. For each test case,
    test_sscount should report whether the actual result matches the expected result.

    Examples of code:
    >>>test_sscount(sscount0, 
    testing sscount0
    Checking sses assesses …
    its value 2 is correct!
    '''

    ourString = args.find(' ')
    needle = args[0:ourString]
    haystack = args[ourString+1:]
    result = (f(needle, haystack))

    print ('testing ' + f.__name__)
    print ('Checking ' + args +'...')
    if (expected_result==result):  
        print ('its value ' + str(expected_result) + ' is correct!')
    else:
        print ('its value is incorrect!')
    return None

def main():
    test_sscount(p34.sscount0, 'sses assesses', 2)
    test_sscount(p34.sscount1, 'sses assesses', 2)
    print('\n')
    test_sscount(p34.sscount0, 'sses assesses', 2)
    test_sscount(p34.sscount1, 'sses assesses', 2)
    print('\n')
    test_sscount(p34.sscount0, 'an trans-Panamanian banana', 6)
    test_sscount(p34.sscount1, 'an trans-Panamanian banana', 6)
    print('\n')
    test_sscount(p34.sscount0, 'needle haystack', 0)
    test_sscount(p34.sscount1, 'needle haystack', 0)
    print('\n')
    test_sscount(p34.sscount0, '!!! !!!!!', 3)
    test_sscount(p34.sscount1, '!!! !!!!!', 3)
    print('\n')
    test_sscount(p34.sscount0, 'o pneumonoultramicroscopicsilicovolcanoconiosis', 9)
    test_sscount(p34.sscount1, 'o pneumonoultramicroscopicsilicovolcanoconiosis', 9)
    print('\n')
    test_sscount(p34.sscount0, '', 0)
    test_sscount(p34.sscount1, '', 0)
    print('\n')
    test_sscount(p34.sscount0, 'a ', 0)
    test_sscount(p34.sscount1, 'a ', 0)
    print('\n')
    test_sscount(p34.sscount0, ' abc', 0) #this is correct, but returns incorrect
    test_sscount(p34.sscount1, ' abc', 0)
    print('\n')
    test_sscount(p34.sscount0, 'a a', 1) #this should return 0, not 1
    test_sscount(p34.sscount1, 'a a', 1)

