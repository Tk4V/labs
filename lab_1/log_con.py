def AND(x1, x2):
    if x1 == True and x2 == True:
        return True
    else:
        return False


def OR(x1, x2):
    if x1 == True or x2 == True:
        return True
    else:
        return False


def NOT(x):
    if x == True:
        return False
    else:
        return True


def XOR(x1, x2):
    if x1 == x2:
        return False
    elif x1 == True or x2 == True:
        return True
    else:
        return False


def IMP(x1, x2):
    if NOT(x1) == True or x2 == True:
        return True
    else:
        return False


def EQU(x1, x2):
    if x1 == x2:
        return True
    else:
        return False