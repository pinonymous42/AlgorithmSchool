import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a > b):
        return (1)
    else:
        return (0)

def insertion_sort(bucket: int) -> None:
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and comp(bucket[j], var)):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var

def bucketsort(num: list[int]) -> list[int]: 
    max_value = max(num)
    size = max_value / len(num)

    buckets_list= []
    for x in range(len(num)):
        buckets_list.append([]) 

    for i in range(len(num)):
        if (type(num[i]) == 'float NaN'):
            num[i] = 0
        j = int (num[i] / size)
        if (j != len(num)):
            buckets_list[j].append(num[i])
        else:
            buckets_list[len(num) - 1].append(num[i])

    for z in range(len(num)):
        insertion_sort(buckets_list[z])
            
    ret = []
    for x in range(len (num)):
        ret = ret + buckets_list[x]
    return ret
