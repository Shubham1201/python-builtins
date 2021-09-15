def abs1(y):
    """ This function will convert negetive value to positive works with float, int, string to get float or int but positive.
    --> positive value will return positive. """
    
    st = str(y)
    final = []
    for i in st:
        final.append(i)

    if '-' in final:   
        final.remove('-')

    c = ""
    for i in final:
        c += i

    if '.' not in c:
        return int(c)
    if '.' in c:
        return(float(c))

def all1(para):
    """ THIS FUNCTION WILL RETURN Flase IF ANY ATLEAST 1 OBJECT WILL NOT ITRABLE.
    --> OR YOU CAN SAY THAT IF 'Flase' OR 0 PASSED IN PARAMETER OR ANYT LIST, TUPPLE OR DICT OR SET IT WILL RETURN False
    OTHERWISE RETURN True. """

    if type(para) == list or tuple or set:
        if False in para:
            return False    
    return True

    if type(para) == dict:
        for i in para:
            if False in para.keys():
                return False
        return True

    if type(para) == str:
        return True
    else:
        return Exception(f"{type(para)} is not itrable")

def any1(para):
    """ THIS FUNCTION WILL RETURN True IF ANY ATLEAST 1 OBJECT WILL ITRABLE.
    --> OR YOU CAN SAY THAT IF 'Flase' OR 0 PASSED IN PARAMETER OR ANYT LISTTUPPLE OR DICT OR SET IT WILL RETURN False
    OTHERWISE RETURN True. """
    if type(para) == list or tuple or set:
        it = []
        for i in para:
            if i == False:
                it.append(i)
        if len(it) == len(para):
            return False
        else:
            return True
        
    if type(para) == dict:
        it = []
        for i in para.keys():
            if i == False:
                it.append(i)
        if len(it) == len(para.keys()):
            return False
        else:
            return True
        
    if type(para) == str:
        return True
    else:
        return Exception(f"{type(para)} is not itrable")

def bin1(para):
    """ This function can convert decimal int to binary """
    sr = []
    a = para
    while a:
        sr.append(a%2)
        a = a // 2

    sr = sr[::-1]
    st = [str(x) for x in sr]
    s = ""
    for i in st:
        s += i
    return f"0b{int(s)}"

def len1(para):
    """ find the length of the list or tuple or set or dict or string """
    counter = 0
    for i in para:
        counter += 1
    return counter

def max1(*args):
    """ get max of any itrable
    --> Facts:
            if you pass all arguments like lists or tuple or set so function will compare only first
            list[0] value and give max.
            example:- 
            [1, 3, 2] and [2, 1, 4] so answer will be [2, 1, 4] """
    if len(args) > 1:
        imax = args[0]
        i = 0
        while i < len(args):
            if imax < args[i]:
                imax = args[i]
            i += 1
        return imax

    if len(args) == 1 and type(args) == list or tuple or set:
        i = 0
        a = list(args[0])
        imax = a[0]
        while i < len(a):
            if imax < a[i]:
                imax = a[i]
            i += 1
        return imax

def min1(*args):
    """ get min of any itrable
    --> Facts:
            if you pass all arguments like lists or tuple or set so function will compare only first
            list[0] value and give min.
            example:- 
            [1, 3, 2] and [2, 1, 4] so answer will be [1, 3, 2] """
    if len(args) > 1:
        imin = args[0]
        i = 0
        while i < len(args):
            if imin > args[i]:
                imin = args[i]
            i += 1
        return imin

    if len(args) == 1 and type(args) == list or tuple or set:
        i = 0
        a = list(args[0])
        imin = a[0]
        while i < len(a):
            if imin > a[i]:
                imin = a[i]
            i += 1
        return imin