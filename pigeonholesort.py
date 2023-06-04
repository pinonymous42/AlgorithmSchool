import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a > b):
        return (1)
    else:
        return (0)

def pigeonholesort(num):
    min_val = min(num)
    max_val = max(num)
    size = max_val - min_val + 1
    holes = []
    for i in range(size):
        holes.append(0)
    for x in num:
        holes[x - min_val] += 1
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            num[i] = count + min_val
            i += 1
    return (num)
