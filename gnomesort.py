import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a >= b):
        return (1)
    else:
        return (0)

def gnomesort(num: list[int]) -> list[int]:
    i = 0
    while i < len(num):
        if (i == 0):
            i += 1
        if (comp(num[i], num[i - 1]) == 1):
            i += 1
        elif (comp(num[i], num[i - 1]) == 0):
            num[i], num[i - 1] = num[i - 1], num[i]
            g.swap += 1
            i -= 1
    return num