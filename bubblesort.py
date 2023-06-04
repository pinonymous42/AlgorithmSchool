import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a > b):
        return (1)
    else:
        return (0)

def bubblesort(num: list[int]) -> list[int]:
    for i in range(len(num)):
        for j in range(len(num) - i - 1):
            if (comp(num[j], num[j + 1])):
                num[j], num[j + 1] = num[j + 1], num[j]
                g.swap += 1
    return (num)