import datetime

def calendar(month, year):
    '''
    (int,int)-> calendar

    Takes two parameters, a month, and a year, and prints
    out the corresponding calendar for that specific
    month and year. Returns none

    Examples of code:
    >>> calendar(10,2019)
    Oct 2019
    Su Mo Tu We Th Fr Sa
           1  2  3  4  5 
     6  7  8  9 10 11 12 
    13 14 15 16 17 18 19 
    20 21 22 23 24 25 26 
    27 28 29 30 31

    >>> calendar(2,2020)
    Feb 2020
    Su Mo Tu We Th Fr Sa
                       1 
     2  3  4  5  6  7  8 
     9 10 11 12 13 14 15 
    16 17 18 19 20 21 22 
    23 24 25 26 27 28 
    '''
    

    adate = datetime.date(year, month, 1) #First day of month of that year

    # Monday = 1 ... Sunday = 7
    startday = adate.isoweekday()

    startday%=7 #SUNDAY = 0, SATURDAY = 6
    MONTHS_DAYS = '31 28 31 30 31 30 31 31 30 31 30 31 '
    MONTHS_NAMES = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'

    ourMonth = MONTHS_NAMES[4*(month-1):4*(month-1)+3] #Start of slice
    daysOfMonth = MONTHS_DAYS[3*(month-1):3*(month-1)+2]

    print(ourMonth +' ' + str(year))

    print('Su Mo Tu We Th Fr Sa')
    print ('   '  *startday,end='')
    days = 1

    for x in range(startday,7):
        print(f' {days} ',end='')
        days+=1
    print()


    numFullWeeks = (int(daysOfMonth)-days)//7  
    for j in range(numFullWeeks):
        for x in range(7):
             print(f'{days:>2} ', end='')
             days+=1
        print()

    for x in range (days,int(daysOfMonth)+1):
        print(f'{days:>2} ', end='')
        days+=1
    print()

    return None


def main():
    print(calendar(12,2019))
    print()
    print(calendar(2,2014))

    
    

    

    


