def len1(para):
    """ find the length of the list or tuple or set or dict or string """
    counter = 0
    for i in para:
        counter += 1
    return counter

# example
# x = (2, 3, 5, 1)
# res = len1(x)
# print(res)