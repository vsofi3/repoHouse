'''
CIS 210 W20 Project 3-4: Python Strings/Counting Substrings

Author: Sofia Vinas

Credits: CS Circles

This program will construct functions to return the count of all
the occurrences of a substring in a string, first using the string slice
operator and then using a string method.
'''
import doctest

def sscount0(needle,haystack):
    '''
    (string,string)-> int

    Returns the number of times that a substring occurs in another string.
    Takes two parameters, needle, the substring to search for, and haystack,
    the string to search in.

    Examples of code:
    >>> sscount0('sses', 'assesses')
    2
    >>> sscount0('!!!', '!!!!!')
    3
    '''
    count = 0
    lengthSubstring = len(needle)
    lengthHaystack = len(haystack)
    for x in range (lengthHaystack):
        newString = haystack[x:lengthSubstring]
        lengthSubstring+=1
        if (newString==needle):
            count+=1

    return count

def sscount1(needle,haystack):
    '''
    (string,string)-> int

    Uses the string method
    starts with (along with other Python tools, e.g., for loop, conditional)
    to implement the same functionality as sscount0.

    Examples of code:
    >>> sscount0('sses', 'assesses')
    2
    >>> sscount0('!!!', '!!!!!')
    3
    '''

    count = 0
    lengthHaystack = len(haystack)
    lengthNeedle = len(needle)
    for x in range (lengthHaystack):
        if (haystack[x:].startswith(needle)):
            count+=1

    return count

print(doctest.testmod())    
    
