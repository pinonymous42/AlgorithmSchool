import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a > b):
        return (1)
    else:
        return (0)

def strand(num: list[int]) -> list[int]:
    element, sub = 0, [num.pop(0)]
    while (element < len(num)):
        if (comp(num[element], sub[-1]) == 1):
            sub.append(num.pop(element))
        elif (comp(num[element], sub[-1]) == 0):
            element += 1
    return sub
  
def merge(a: int, b: int) -> list[int]:
    ret = []
    while (len(a) and len(b)):
        if (comp(b[0], a[0]) == 1):
            ret.append(a.pop(0))
        else:
            ret.append(b.pop(0))
    ret += a
    ret += b
    return ret

def strandsort(num: list[int]) -> list[int]:
    ret = strand(num)
    while (len(num)):
        ret = merge(ret, strand(num))
    return ret