import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a >= b):
        return (1)
    else:
        return (0)

def divide(num: list[int], start: int, end: int) -> list[int]:
    i = start - 1
    pivot = num[end]
    for j in range(start, end):
        if (comp(pivot, num[j]) == 1):
            i += 1
            num[i], num[j] = num[j], num[i]
            g.swap += 1
    num[i + 1], num[end] = num[end], num[i + 1]
    g.swap += 1
    return i + 1

def quicksorthelper(num: list[int], start: int, end: int) -> list[int]:
    if start < end:
        pivot_index = divide(num, start, end)
        quicksorthelper(num, start, pivot_index - 1)
        quicksorthelper(num, pivot_index + 1, end)
    return num

def quicksort(num: list[int]) -> list[int]:
    start = 0
    end = len(num) - 1
    num = quicksorthelper(num, start, end)
    return num