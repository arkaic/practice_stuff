# In-place quicksorting

def quicksort_inplace(a, l, r):
    def partition(a, start, end):
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