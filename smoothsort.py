import global_value as g

g.swap = 0
g.cmp = 0

def comp(a:int, b: int) -> int:
    g.cmp += 1
    if (a >= b):
        return (1)
    else:
        return (0)

_leonardo_nums = [1, 1]

def L(k):
    try:
        return _leonardo_nums[k]
    except IndexError:
        while len(_leonardo_nums) <= k:
            _leonardo_nums.append(_leonardo_nums[-2] + _leonardo_nums[-1] + 1)
        return _leonardo_nums[k]

def smoothsort(num):
    size_list = _create_heap(num)
    _sort_heap(num, size_list)
    return num

def _sort_heap(heap, size_list):
    for heap_size in reversed(range(len(heap))):
        _dequeue_max(heap, size_list, heap_size)

def _dequeue_max(heap, size_list, heap_size):
    removed_size = size_list.pop()
    if removed_size == 0 or removed_size == 1:
        pass
    else:
        size_list.append(removed_size - 1)
        size_list.append(removed_size - 2)
        left_idx = heap_size - L(size_list[-1]) - 1
        right_idx = heap_size - 1
        left_size_idx = len(size_list) - 2
        right_size_idx = len(size_list) - 1
        idx, size_idx = _fix_roots(heap, size_list, left_idx, left_size_idx)
        _sift_down(heap, idx, size_list[size_idx])
        idx, size_idx = _fix_roots(heap, size_list, right_idx, right_size_idx)
        _sift_down(heap, idx, size_list[size_idx])

def _create_heap(num):
    size_list = []
    for heap_end in range(len(num)):
        _add_new_root(size_list)

        idx, size_idx = _fix_roots(num, size_list, heap_end, len(size_list) - 1)

        _sift_down(num, idx, size_list[size_idx])

    return size_list

def _add_new_root(size_list):
    if len(size_list) == 0:
        size_list.append(1)
    elif len(size_list) > 1 and size_list[-2] == size_list[-1] + 1:
        size_list[-2] = size_list[-2] + 1
        del size_list[-1]
    else:
        if size_list[-1] == 1:
            size_list.append(0)
        else:
            size_list.append(1)


def _fix_roots(heap, sizes, start_heap_idx, start_size_idx):
    cur = start_heap_idx
    size_cur = start_size_idx
    while size_cur > 0:
        next = cur - L(sizes[size_cur])
        if (comp(heap[cur], heap[next]) == 1):
            break
        if sizes[size_cur] > 1:
            right = cur - 1
            left = right - L(sizes[size_cur]-2)
            if (comp(heap[right], heap[next]) == 1 or comp(heap[left], heap[next]) == 1):
                break

        temp = heap[cur]
        heap[cur] = heap[next]
        heap[next] = temp
        size_cur = size_cur - 1
        cur = next
    return (cur, size_cur)


def _sift_down(heap, root_idx, tree_size):
    cur = root_idx
    while tree_size > 1:
        right = cur - 1
        left = cur - 1 - L(tree_size - 2)
        if (comp(heap[cur], heap[left]) == 1 and comp(heap[cur], heap[right]) == 1):
            break
        elif (comp(heap[right], heap[left]) == 1):
            heap[cur], heap[right] = heap[right], heap[cur]
            g.swap += 1
            cur = right
            tree_size = tree_size - 2
        else:
            g.cmp += 1
            heap[cur], heap[left] = heap[left], heap[cur]
            cur = left
            tree_size = tree_size - 1