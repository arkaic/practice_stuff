# In-place quicksorting

def _partition(a, start, end):
    """ Pivot substitutes with the left pointer
    """

    p = start
    l = p + 1
    r = end

    if len(a) < 2:
        return a

    while l < r:
        while l < r and a[l] <= a[p]:
            l += 1
        while r > l and a[p] < a[r]:
            r -= 1
        temp = a[l]
        a[l] = a[r]
        a[r] = temp

    if a[l] <= a[p]:
        temp = a[l]
        a[l] = a[p]
        a[p] = temp
        return l
    else:
        temp = a[l - 1]
        a[l - 1] = a[p]
        a[p] = temp
        return l - 1

def quicksort_inplace(a, l, r):
    if l == r:
        return a

    pivot = _partition(a, l, r)

    if pivot > l:
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
