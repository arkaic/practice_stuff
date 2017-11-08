# All sorts in ascending order

def insertionsort(l):
    """
    In place insertion sort

    Returns:
        a list
    """
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
    """
    Returns:
        a list
    """
    m = []
    while l:
        small = None
        for x in l:
            if small is None or x < small:
                small = x
        m.append(l.pop(l.index(small)))
    return m

def quicksort_inplace(a, l, r):
    """
    Implementation operates in place

    Args:
        a - list to be sorted
        l - integer index for left side
        r - integer index for right side

    Returns:
        a list
    """
    if l != r:
        pivot = _partition(a, l, r)
        if l < pivot:
            quicksort_inplace(a, l, pivot - 1)
        if pivot < r:
            quicksort_inplace(a, pivot + 1, r)

    return a

def _partition(a, start, end):
    """
    In-place partitioning using a[start] as pivot

    Args:
        a      - list
        start  - integer index
        end    - integer index

    Returns:
        an integer index for final location of pivot
    """
    piv = start
    left = start + 1
    right = end

    if len(a) < 2:
        return a

    # goal: keep this pattern [LTE, .., pivot, .., GT]
    # Two index pointers left and end move towards each other and swap any elements
    # to fit above pattern. End this loop when they touch to determine location of pivot
    while left < right:
        while left < right and a[left] <= a[piv]:
            left += 1
        while left < right and a[right] > a[piv]:
            right -= 1
        temp = a[left]
        a[left] = a[right]
        a[right] = temp

    # determine final pivot location
    if a[left] <= a[piv]:
        final_piv = left
    else:
        final_piv = left - 1

    # swap places with pivot subs
    temp = a[final_piv]
    a[final_piv] = a[piv]
    a[piv] = temp

    return final_piv

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


