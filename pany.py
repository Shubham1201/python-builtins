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

# Example
# x = {0: 'zero'}
# res = any1(x)
# print(res)

