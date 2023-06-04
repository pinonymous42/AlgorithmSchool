import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a > b):
        return (1)
    else:
        return (0)

def is_minus(value: int) -> int:
    if (value < 0):
        return (1)
    else:
        return (0)
    # return (value < 0)

def max(n1: int, n2: int) -> int:
    if (comp(n1, n2) == 1):
        return (n1)
    elif (comp(n1, n2) == 0):
        return (n2)

def min(n1: int, n2: int) -> int:
    if (comp(n1, n2) == 1):
        return (n2)
    elif (comp(n1, n2) == 0):
        return (n1)
    
def prepareLibrarySort(epsilon: int, n: int, num: list[int]) -> int:
    length = (1 + epsilon) * n
    for i in range(length):
        num.append(-1)
    return (length)

def binary_search(value: int, num: list[int], last: int) -> int:
    first = 0
    while (last >= 0 and is_minus(num[last])):
        last -= 1
    while (first <= last and is_minus(num[first])):
        first += 1
    while (first <= last):
        middle = int((first + last) / 2)
        if (is_minus(num[middle])):
            tmp = middle + 1
            #Look to the right
            while (tmp < last and is_minus(num[tmp])):
                tmp += 1
            if (comp(num[tmp], value) == 1):
                tmp = middle - 1
                while (middle > first and is_minus(num[middle])):
                    middle -= 1
                #Look to the left
                if (comp(num[middle], value) == 1):
                    return (middle)
                last = middle - 1
            else:
                first = tmp + 1
        elif (num[middle] < value):
            first = middle + 1
        else:
            last = middle - 1
    if (last >= 0 and is_minus(num[last])):
        last -= 1
    return (last)

def libSort(num: list[int], N: int, new: list[int], EPSILON: int) -> None:
    if(N == 0):
        return
 
    # ------ BASE CASE ------
    goal = 1
    pos = 1
 
    new[0] = num[0]
 
    sLen = max((1 + EPSILON), goal + 1)
 
    # ------ CONDITION -------
    while(pos < N):
        # ------ ROUND ------
        for j in range(goal):
            insPos = binary_search(num[pos], new, sLen - 1)
 
            insPos += 1
            if (is_minus(new[insPos]) == 0):
                nextFree = insPos + 1
                while(is_minus(new[nextFree]) == 0):
                    nextFree += 1
                if (nextFree >= sLen):
                    insPos -= 1
                    if(is_minus(new[insPos]) == 0):
                        
                        nextFree = insPos - 1
                        while (is_minus(new[nextFree]) == 0):
                            nextFree -= 1
                        while (nextFree < insPos):
                            new[nextFree] = new[nextFree + 1]
                            nextFree += 1
                else:
                    while (nextFree > insPos):
                        new[nextFree] = new[nextFree - 1]
                        nextFree -= 1
            elif (insPos >= sLen):
                insPos -= 1
                nextFree = insPos - 1
                while (is_minus(new[nextFree]) == 0):
                    nextFree -= 1
                while (nextFree < insPos):
                    new[nextFree] = new[nextFree + 1]
                    nextFree += 1

            new[insPos] = num[pos]
            pos += 1
 
            if (pos >= N):
                return
 
        # ----- REBALANCE -----
        j = sLen - 1
        k = int(min(goal * (2 + 2 * EPSILON), (1 + EPSILON) * N) - 1)
        step = int((k + 1) / (j + 1))
        while (j >= 0):
            new[k] = new[j]
            new[j] = -1
            j -= 1
            k -= step
 
        sLen = int(min(goal * (2 + 2 * EPSILON), N * (1 + EPSILON)))
        goal <<= 1

def librarysort(num: list[int]) -> list[len]:
   epsilon = 1
   new = []
   size = len(num)
   #This takes linear time
   length = prepareLibrarySort(epsilon, size, new)
   #O (n log n)
   libSort(num, size, new, epsilon)
   #This takes linear time
   i = 0
   j = 0
   while (i < length and j < size):
       if (is_minus(new[i]) == 0):
           num[j] = new[i]
           j += 1
       i += 1
   return (num)