def majors_readf(fname):
    '''
    (string)->list

    Takes one parameter, a string which is the name of the majors file.
    The function then opens the file and creates and returns a list of the
    majors in this file.

    Examples of code:
    >>> majors_readf('majors-short.txt')
    ['PBA', 'CIS', 'EC', 'CIS', 'EXPL', 'CIS', 'EXPL','EXPL', 'MACS']
    '''
    with open(fname,'r') as myf:
        listOfMajors = myf.readlines()
        listOfMajors = listOfMajors[2:]
        newList = []
        for x in range(len(listOfMajors)):
            myLiValue = listOfMajors[x].strip()
            newList.append(myLiValue)
            
        return newList #This looks like it works for now


def majors_analysis(majorsli):
    '''
    (list)-> tuple

    Takes one parameter, a list of majors, and determines the most frequently
    ocurring major(s) (mode) in the argument list, and also the count of
    the number of distinct majors in the list. Returns a tuple of the results.

    Examples of code:
    >>> majors_analysis(['CIS', 'CIS', 'EXPL', 'COLT', 'EXPL'])
    (['CIS', 'EXPL'], 3)
    '''
    distinctMajors = 0
    for j in range (1,len(majorsli)):
        if majorsli[j] != majorsli[j-1]:
            distinctMajors+=1        
    print (distinctMajors) #This part of the function works for now
        
    countdict = [] #now we want to create the list for the mode
    for item in majorsli:
        if item in countdict:
            countdict[item] = item

    
    return (itemList, distinctMajors)
    
