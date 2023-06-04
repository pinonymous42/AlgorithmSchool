import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a > b):
        return (1)
    else:
        return (0)

def insertionsort(num: list[int]) -> list[int]:
    for i in range(1, len(num)):
        tmp = num[i]
        j = i - 1
        while (j >= 0 and comp(num[j], tmp) == 1):
            num[j + 1] = num[j]
            j -= 1
        num[j + 1] = tmp
    return (num)