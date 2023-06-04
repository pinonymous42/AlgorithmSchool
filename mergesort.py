import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a >= b):
        return (1)
    else:
        return (0)

def mergesort(num: list[int]) -> list[int]:
    if (len(num) <= 1):
        return num
    split = len(num) // 2
    left = num[:split]
    right = num[split:]

    left = mergesort(left)
    right = mergesort(right)

    i, j, k= 0, 0, 0
    while (i < len(left) and j < len(right)):
        if (comp(right[j], left[i]) == 1):
            num[k] = left[i]
            i += 1
        elif (comp(right[j], left[i]) == 0):
            num[k] = right[j]
            j += 1
        k += 1

    while (i < len(left)):
        num[k] = left[i]
        i += 1
        k += 1
    while (j < len(right)):
        num[k] = right[j]
        j += 1
        k += 1
    return num