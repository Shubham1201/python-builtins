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

# Example
# y = abs1(-1.20)
# print(y)