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
    
# example
# x = 536
# res = bin1(x)
# print(res)