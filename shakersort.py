import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a > b):
        return (1)
    else:
        return (0)

def shakersort(num: list[int]) -> list[int]:
    start = 0
    end  = len(num) - 1

    while (start < end):
        for i in range(start, end):
            if (comp(num[i], num[i + 1]) == 1):
                g.swap += 1
                num[i], num[i + 1] = num[i + 1], num[i]
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if (comp(num[i], num[i + 1]) == 1):
                g.swap += 1
                num[i], num[i + 1] = num[i + 1], num[i]
    return (num)