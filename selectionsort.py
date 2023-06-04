import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a > b):
        return (1)
    else:
        return (0)

def selectionsort(num: list[int]) -> list[int]:
    for i in range(len(num)):
        min = i
        for j in range(i + 1, len(num)):
            if (comp(num[min], num[j]) == 1):
                min = j
        num[i], num[min] = num[min], num[i]
        g.swap += 1
    return (num)