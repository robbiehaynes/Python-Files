#Rob Haynes
#10 May 2021

def gumatj_to_decimal(a):
    if len(str(a)) > 1:
        a_str = str(a)

        fives = eval(a_str[:1])
        singles = eval(a_str[1:])

        return fives*5 + singles
    else:
        return a

def decimal_to_gumatj(a):
    fives = int(a/5)
    singles = a%5
    if fives != 0:
        gumatj = str(fives)+str(singles)
    else:
        gumatj = str(singles)
    
    return eval(gumatj)

def gumatj_add(a, b):
    a2 = gumatj_to_decimal(a)
    b2 = gumatj_to_decimal(b)
    c = a2 + b2
    return decimal_to_gumatj(c)

def gumatj_multiply(a, b):
    a2 = gumatj_to_decimal(a)
    b2 = gumatj_to_decimal(b)
    c = a2 * b2
    return decimal_to_gumatj(c)
