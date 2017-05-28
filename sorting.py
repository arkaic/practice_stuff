""" All sorts in ascending order """

def insertionsort(l):
    ptr = 1
    while ptr < len(l):
        c = ptr
        while c > 0 and l[c] < l[c - 1]:
            tmp = l[c]
            l[c] = l[c - 1]
            l[c - 1] = tmp
            c -= 1
        ptr += 1
    return l

def selectsort(l):
    m = []
    while l:
        small = None
        for x in l:
            if small is None or x < small:
                small = x
        m.append(l.pop(l.index(small)))
    return m

def quicksort_inplace(a, l, r):
    """ Implementation uses the same list """

    def partition(a, start, end):
        """ Pivot substitutes with the left pointer """
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

        if a[l] <= a[p]: swap = l
        else: swap = l - 1
        temp = a[swap]
        a[swap] = a[p]
        a[p] = temp

        return swap
    # ----------------------------END NESTED FUNCTION --------------------------

    if l == r: return a

    pivot = partition(a, l, r)
    if l < pivot:
        quicksort_inplace(a, l, pivot - 1)
    if pivot < r:
        quicksort_inplace(a, pivot + 1, r)

    return a


def mergesort(l):
    def merge(m, n):
        l = []
        while m and n:
            if m[0] <= n[0]: l.append(m.pop(0))
            else: l.append(n.pop(0))
        if m: l.extend(m)
        elif n: l.extend(n)
        return l

    if len(l) < 2: return l

    middle = int(len(l) / 2)
    m = mergesort(l[:middle])
    n = mergesort(l[middle:])
    return merge(m, n)

def heapsort(l):
    """ In place sorting exploiting the heap property of indices in a binary 
    tree.
    """
    def swap(i, j):
        tmp = l[i]
        l[i] = l[j]
        l[j] = tmp

    def heap_up(i):
        if i != 0:
            parent = int((i - 1) / 2)
            if l[i] > l[parent]:
                swap(i, parent)
                heap_up(parent)

    def heap_down(i, heap_divider):
        left, right = i * 2 + 1, i * 2 + 2
        if i < heap_divider and left < heap_divider:
            choice = None
            if l[i] < l[left]:
                if right < heap_divider and l[i] < l[right]:
                    choice = left if l[left] > l[right] else right
                else:
                    choice = left
            elif right < heap_divider and l[i] < l[right]:
                choice = right
            if choice is not None:
                swap(i, choice)
                heap_down(choice, heap_divider)

    # ---------------------- END NESTED FUNCTIONS ------------------------------

    # First, order l into a heap. The heap will build up as the left side of the
    # list using a pointer, the heap_divider, to mark the division line. The ptr
    # will start from the left side and end on the right side, denoting that the
    # heap is built. Throughout the heap building, the pointer points to the item
    # that needs to be heaped up.
    heap_divider = 0  # index of position immediately right of heap
    while heap_divider < len(l):
        heap_up(heap_divider)
        heap_divider += 1

    # Second, build the output list by moving the heap_divider back to the left.
    # Specifically, swap the first item with the current heap_divider, heap down
    # the new first item, then move the pointer left by one.
    heap_divider -= 1
    while heap_divider > 0:
        swap(0, heap_divider)
        heap_down(0, heap_divider)
        heap_divider -= 1
    return l


