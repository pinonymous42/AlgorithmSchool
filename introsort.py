import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a > b):
        return (1)
    else:
        return (0)

def max_heapify(num: list[int], index: int, start: int, end: int) -> None:
    def left(i):
        return 2 * i + 1
    def right(i):
        return 2 * i + 2

    size = end - start
    l = left(index)
    r = right(index)
    if (l < size and comp(num[start + l], num[start + index]) == 1):
        largest = l
    else:
        largest = index
    if (r < size and comp(num[start + r], num[start + largest]) == 1):
        largest = r
    if largest != index:
        swap(num, start+largest, start+index)
        max_heapify(num, largest, start, end)

def swap(num: list[int], i: int, j: int) -> None:
    num[i], num[j] = num[j], num[i]
    g.swap += 1

def build_max_heap(num: list[int], start: int, end: int) -> None:
    def parent(i):
        return (i-1)//2
    length = end - start
    index = parent(length - 1)
    while (index >= 0):
        max_heapify(num, index, start, end)
        index -= 1

def heapsort(num: list[int], start: int, end: int) -> None:
    build_max_heap(num, start, end)
    for i in range(end - 1, start, -1):
        swap(num, start, i)
        max_heapify(num, index=0, start=start, end=i)

def partition(num: list[int], start: int, end: int) -> None:
    pivot = num[start]
    i = start - 1
    j = end

    while (True):
        i += 1
        while (comp(pivot, num[i]) == 1):
            i += 1
        j -= 1
        while (comp(pivot, num[j]) == 1):
            j -= 1
        if (i >= j):
            return j
        swap(num, i, j)

def introsort_helper(num: list[int], start: int, end: int, maxdepth: int) -> None:
    if (end - start <= 1):
        return
    elif (maxdepth == 0):
        heapsort(num, start, end)
    else:
        p = partition(num, start, end)
        introsort_helper(num, start, p+1, maxdepth - 1)
        introsort_helper(num, p+1, end, maxdepth - 1)

def introsort(num: list[int]) -> list[int]:
    maxdepth = (len(num).bit_length() - 1) * 2
    introsort_helper(num, 0, len(num), maxdepth)
    return (num)
