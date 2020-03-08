import doctest

def mean(alist):
    '''
    (list)-> float

    Takes a list of numbers and returns the mean as a float

    Examples of code:
    >>>mean([1,2,3,4,5])
    3.0
    >>>mean([4,56,7,99,8,0])
    29.0
    '''
    mean=sum(alist)/len(alist)
    return mean

def median(alist):
    '''
    (list)-> int

    Takes a list of numbers and returns the median as an integer

    Examples of code:
    >>>median([1,2,3,4,5])
    3
    >>>median([4,56,7,99,8,0])
    7.5
    '''
    copylist=alist[:]
    copylist.sort()
    if isEven(len(alist)): #REVISION TO MEDIAN FUNCTION- CALLS isEven function now
        rightmid = len(copylist)//2
        leftmid = rightmid-1
        median = (copylist[leftmid] + copylist[rightmid])/2
    else:
        mid = len(copylist)//2
        median = copylist[mid]
    return median

def mode(alist):
    '''
    (list)-> list

    Takes a list of numbers and returns the mode as an integer. Returns
    first integers in the list if nothing else occurs more often.

    Examples of code:
    >>>mode([1,1,2,3,4])
    1
    >>>mode([4,56,7,99,8,0])
    4
    '''
    '''
    max_count = (0,0)
    for num in alist:
        occurences = alist.count(num)
        if occurences>max_count[0]:
            max_count = (occurences,num)
    return max_count[1]
    '''

#REVISION TO mode function to call genFrequencyTable
    dictionary = genFrequencyTable(alist)
    marker = []
    key = list(dictionary.values())
    maxValue = max(key)
    for item in dictionary:
        if dictionary.get(item) == maxValue:
            marker.append(item)
    return marker

def frequencyTable(alist):
    '''
    (list)-> table

    Takes a list of numbers and returns a table that shows all of the integers
    that appear in the list, as well as the number of times they show up in
    the list.

    Examples of code:
    >frequencyTable([1,3,3,2])
    ITEM FREQUENCY
    1          1
    2          1
    3          2
    '''
    countdict = {}
    '''
    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item]+1
        else:
            countdict[item] = 1

    itemlist = list(countdict.keys())
    itemlist.sort()

    print('ITEM', 'FREQUENCY')

    for item in itemlist:
        print (item, '        ', countdict[item])
    '''

#REVISION TO frequencyTable function to call genFrequencyTable
    dictionary = genFrequencyTable(alist)
    print('ITEM',  'FREQUENCY')
    for item in dictionary:
        print (item, '      ' ,dictionary.get(item))

def isEven(n):
    '''
    (int)-> boolean

    Takes an integer n, and returns True if even, False if odd.

    Examples of code:
    >>>isEven(4)
    True
    >>>isEven(5)
    False
    '''
    if (n%2==0):
        return True
    else:
        return False

#I'M NOT SURE HOW TO DO THE DOCTEST.TESTMOD()

def genFrequencyTable(alist):
    '''
    (list)-> table

    Takes a list of numbers and generates the dictionary frequency counts that
    are currently being generated in the mode and frequency table function.
    The function will return a dictionary.

    Examples of code:
    >>> genFrequencyTable([1, 2, 3, 3, 1, 4, 5])
    {1:2, 2:1, 3:2, 4:1, 5:1}
    >>> genFrequencyTable([4,5,0,0,89,3,44])
    {4: 1, 5: 1, 0: 2, 89: 1, 3: 1, 44: 1}
    '''
    newDictionary={}
    countdict={}
    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item]+1
        else:
            countdict[item] = 1

    for item in alist:
        newDictionary[item] = countdict[item]
    return newDictionary

def main():
    alist = [5.3, 3.0, 2.6, 4.4, 2.9, 4.8, 4.3,
    2.6, 2.9, 4.9, 2.5, 4.8, 4.2, 2.6,
    4.8, 2.7, 5.0, 2.7, 2.8, 4.3, 3.1,
    4.1, 2.8, 5.8, 2.5, 3.9, 4.8, 2.9,
    2.5, 4.9, 5.0, 2.5, 3.2, 2.6, 2.7,
    4.8, 4.1, 5.1, 4.7, 2.6, 2.9, 2.7,
    3.3, 3.0, 4.4, 2.7, 5.7, 2.5, 5.1,
    2.5, 4.4, 4.6, 5.7, 4.5, 4.7, 5.1,
    2.9, 3.3, 2.7, 2.8, 2.9, 2.6, 5.3,
    6.0, 3.0, 5.3, 2.7, 4.3, 5.4, 4.4,
    2.6, 2.8, 4.4, 4.3, 4.7, 3.3, 4.0,
    2.5, 4.9, 4.9, 2.5, 4.8, 3.1, 4.9,
    4.4, 6.6, 3.3, 2.5, 5.0, 4.8, 2.5,
    4.2, 4.5, 2.6, 4.0, 3.3, 3.1, 2.6,
    2.7, 2.9, 2.7, 2.9, 3.3, 2.8, 3.1,
    2.5, 4.3, 3.2, 4.6, 2.8, 4.8, 5.1,
    2.7, 2.6, 3.1, 2.9, 4.2, 4.8, 2.5,
    4.5, 4.5, 2.8, 4.7, 4.6, 4.6, 5.1,
    4.2, 2.8, 2.5, 4.5, 4.6, 2.6, 5.0,
    2.8, 2.9, 2.7, 3.1, 2.6, 2.5, 3.2,
    3.2, 5.2, 2.8, 3.2, 2.6, 5.3, 5.5,
    2.7, 5.2, 6.4, 4.2, 3.1, 2.8, 4.5,
    2.9, 3.1, 4.3, 4.9, 5.2, 2.6, 6.7,
    2.7, 4.9, 3.0, 4.9, 4.7, 2.6, 4.6,
    2.5, 3.2, 2.7, 6.2, 4.0, 4.6, 4.9,
    2.5, 5.1, 3.3, 2.5, 4.7, 2.5, 4.1,
    3.1, 4.6, 2.8, 3.1, 6.3]

    x = mean(alist)
    print(x)

    j = median(alist)
    print(j)

    y = mode(alist)
    print(y)
    print()
    frequencyTable(alist)

    
    
