def parity(bitrep):
    '''
    (str)-> str (1 character)

    Takes one parameter, a string of 0's and 1's, and will
    return a 1-character string, the parity bit.

    Examples of code:
    >>> parity('1100011')
    '0'
    >>> parity('1100100')
    '1'
    '''
    manipulatedValue = bitrep
    manipulatedBitRep = manipulatedValue.count('1') #counts the number of 1's 
    if ((manipulatedBitRep%2)==0):
        return '0'
    else:
        return '1'


def encode(letter):
    '''
    (str)-> str(in binary form)
    
    Takes one parameter, letter, a string. The function will
    add a parity bit to the binary (ASCII) representation of
    letter. The parity bit should be the most significant
    (leftmost) character. The new binary representation will
    be returned

    Examples of code:
    >>> encode('c')
    '01100011'
    >>> encode('d')
    '11100100'
    '''
    singleDigit = parity(bin(ord(letter)))
    value = str(bin(ord(letter)))
    if singleDigit=='0':
        return (singleDigit+value[2:])
    else:
        return (singleDigit+value[2:])


def decode(pletter):
    '''
    (str)-> str

    Takes one parameter, pletter, a string representing the
    binary sequence, plus parity bit, for a character. The
    function should call parity, to check for even parity in
    pletter. If no error is detected, decode should convert
    pletter back to character, and return the character. If
    an error is detected, decode should return '*'.

    Examples of code:
    >>> decode('01100011')
    'c'
    >>> decode('11100100')
    '*'
    '''
    #we want to subtract parity bit from pletter
    binaryRep = pletter[1:]
    if (parity(binaryRep)=='0'): #means even parity
        return chr(int(binaryRep,2))
    else:
        return '*' #means odd parity


def main():
    word = 'spider'
    for letter in word:
        sample = encode(letter)
        print(decode(sample), end='')
    print()
    word = 'capital'
    for x in word:
        sample = encode(x)
        print(decode(sample), end='')
    print()
    return None

if __name__=='__main__':
    main()

 
        

    
    

    

