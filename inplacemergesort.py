import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a >= b):
        return (1)
    else:
        return (0)

def mergeInPlace(num: list[int], left: int, middle: int, right: int):
   mx = max(num[middle], num[right]) + 1

   i, j, k = left, middle + 1, left
   while (i <= middle and j <= right and k <= right):
       e1 = num[i] % mx
       e2 = num[j] % mx
       if (comp(e2, e1) == 1):
           num[k] += (e1 * mx)
           i += 1
           k += 1
       elif (comp(e2, e1) == 0):
           num[k] += (e2 * mx)
           j += 1
           k += 1

   while (i <= middle):
       el = num[i] % mx
       num[k] += (el * mx)
       i += 1
       k += 1

   while (j <= right):
       el = num[j] % mx
       num[k] += (el * mx)
       j += 1
       k += 1

   for i in range(left, right + 1):
       num[i] //= mx


def inplacehelper(num: list[int], left: int, right: int) -> list[int]:
    if left < right:
        middle = left + (right - left) // 2
 
        inplacehelper(num, left, middle)
        inplacehelper(num, middle + 1, right)
        mergeInPlace(num, left, middle, right)
    return (num)

def inplacemergesort(num: list[int]) -> list[int]:
    left = 0
    right = len(num) - 1
    num = inplacehelper(num, left, right)
    return (num)