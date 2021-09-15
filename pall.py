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

# Example
# x = {1, 11, 34, "True"}
# res = all1(x)
# print(res)
