# In-place quicksorting

def _partition(a, start, end):
    """ Pivot substitutes with the left pointer
    """

    p = start
    l = p + 1

    if len(a) < 2:
        return a

    while l < end:
        while l < end and a[l] <= a[p]:
            l += 1
        while end > l and a[p] < a[end]:
            end -= 1
        temp = a[l]
        a[l] = a[end]
        a[end] = temp

    if a[l] <= a[p]:
        swap = l
    else:
        swap = l - 1
    temp = a[swap]
    a[swap] = a[p]
    a[p] = temp

    return swap

def quicksort_inplace(a, l, r):
    if l == r:
        return a

    pivot = _partition(a, l, r)

    if l < pivot:
        quicksort_inplace(a, l, pivot - 1)
    if pivot < r:
        quicksort_inplace(a, pivot + 1, r)

    return a


################################################################################
################################################################################

import random, sys
# sys.setrecursionlimit(10)

if len(sys.argv) == 2:
    a = [random.randrange(0, 100) for x in range(int(sys.argv[1]))]
    print('{}\n'.format(a))
    print('\n{}'.format(quicksort_inplace(a, 0, len(a) - 1)))
