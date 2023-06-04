import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a > b):
        return (1)
    else:
        return (0)

def shellsort(nums: int) -> list[int]:
    gap = len(nums) // 2
    while gap > 0:
        for i in range(gap, len(nums)):
            tmp = nums[i]
            j = i
            while (j >= gap and comp(nums[j - gap], tmp) == 1):
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = tmp
        gap //= 2
    return nums