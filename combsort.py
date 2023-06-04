import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a > b):
        return (1)
    else:
        return (0)

def combsort(num: list[int]) -> list[int]:
    gap = len(num)
    flag = True
    while (gap != 1 or flag):
        gap = int(gap / 1.3)
        if (gap < 1):
            gap = 1
        flag = False
        for i in range(0, len(num) - gap):
            if (comp(num[i], num[i + gap]) == 1):
                g.swap += 1
                num[i], num[i + gap] = num[i + gap], num[i]
                flag = True
    return (num)