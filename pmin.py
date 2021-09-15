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

# example
# x = [2, 5, 2, -1, 6]
# a = min1(x)
# print(a)