from prettytable import PrettyTable

import log_con


# ["a", "b", "!a", "a^b", "a v b", "a→b", "a〜b", "a ⊕ b"]

def f_value(a,b, c=None):
    return [a,b,log_con.NOT(a), log_con.AND(a,b), log_con.OR(a,b), log_con.IMP(a,b), log_con.EQU(a,b), log_con.XOR(a,b)]

def s_value(a, b, c):
    first = log_con.OR(log_con.NOT(a), b)
    second = log_con.NOT(first)
    third = log_con.OR(log_con.NOT(b), c)
    fourth = log_con.AND(second, c)
    return [a,
            b,
            c,
            first,
            second,
            third,
            fourth,
            log_con.EQU(third, fourth)
        ]


def row(n, a, b, c=None):
    if n == 2:
        first_table.add_row(f_value(a,b))
    elif n == 3:
        second_table.add_row(s_value(a, b, c))

def combinations(*args, p=1):
    pairs = [tuple(pair) for pair in args] * p
    result = [[]]
    for i in pairs:
        result = [x + [y] for x in result for y in i]
    return result

# "not(not(a) or b) and c eq (not(b) or c)"

def add_row(n):
    lst = []
    for l in combinations([True, False], p=n):
        d = dict(zip(["a", "b", "c"], l))
        lst.append(d)
    for item in lst:
        row(n, item.get("a"), item.get("b"), item.get("c"))


second_table = PrettyTable()
first_table = PrettyTable()

def variant_7():
 
    second_table.field_names = [
        "a",
        "b",
         "c",
        "not(a) or b",
        "not(not(a) or b)",
        "not(b) or c",
        "not(not(a) or b) and c",
        "not(not(a) or b) and c eq (not(b) or c)"
    ]

    first_table.field_names = ["a", "b", "!a", "a^b", "a v b", "a→b", "a〜b", "a ⊕ b"]
    add_row(2)
    add_row(3)
    print(f"{first_table}\n\n{second_table}")

variant_7()

