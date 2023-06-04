import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a > b):
        return (1)
    else:
        return (0)

def oddevensort(num):
   # flag
   isSorted = 0
   size = len(num)
   while isSorted == 0:
      isSorted = 1
      temp = 0
      for i in range(1, size - 1, 2):
         if (comp(num[i], num[i + 1]) == 1):
            g.swap += 1
            num[i], num[i + 1] = num[i + 1], num[i]
            isSorted = 0
      for i in range(0, size - 1, 2):
         if (comp(num[i], num[i + 1]) == 1):
            g.swap += 1
            num[i], num[i + 1] = num[i + 1], num[i]
            isSorted = 0
   return num