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
# example
# x = [2, 5, 2, -1, 6]
# a = min1(x)
# print(a)