import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a > b):
        return (1)
    else:
        return (0)

def max_heapify(num: list[int], n: int, i: int) -> None:
    largest = i
    left  = 2 * i + 1
    right = 2 * i + 2

    if (left < n and comp(num[left], num[i]) == 1):
        largest = left

    if (right < n and comp(num[right], num[largest]) == 1):
        largest = right

    if (largest != i):
        num[i], num[largest] = num[largest], num[i]
        g.swap += 1

        max_heapify(num, n, largest)

def heapsort(num: list[int]) -> list[int]:
    n = len(num)
    for i in range(n // 2, -1, -1):
        max_heapify(num, n, i)

    for i in range(n - 1, 0, -1):
        num[i], num[0] = num[0], num[i]
        g.swap += 1
        max_heapify(num, i, 0)
    return (num)