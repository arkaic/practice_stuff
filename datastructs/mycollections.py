import argparse, sys, unittest
from math import floor
from random import randrange

class HashtableOA:
    """ Open addressing method """

    _init_size = 97
    l = None
    count = None

    def __init__(self):
        self.l = [None] * self._init_size
        self.count = 0
                
    def get(self, k):
        h = self._hashfunc(k)
        if self.l[h] is None:
            return None
        else:
            return self.l[h][1]

    def put(self, k, v):
        h = self._hashfunc(k)
        if self.l[h] is None:
            self.count += 1
        self.l[h] = (k, v)

        if self.count > .7 * len(self.l):
            # resize
            self.count = 0
            old_l = self.l
            self.l = [None] * (len(old_l) * 2)
            for x in old_l:
                if x is not None:
                    self.put(x[0], x[1])

    def remove(self, k):
        h = self._hashfunc(k)
        pair = self.l[h]
        if pair:
            self.l[h] = None
            self.count -= 1

        if self.count < .2 * len(self.l):
            # resize
            self.count = 0
            old_l = self.l
            self.l = [None] * (len(old_l) / 2)
            for x in old_l:
                if x is not None:
                    self.put(x[0], x[1])

        return pair

    def _hashfunc(self, k):
        """ m <= list_size """
        a = 0.67
        m = len(self.l)  # prime
        h = floor(m * (k * a - floor(k * a)))

        if self.l[h] and self.l[h][0] != k:
            h = self._linear_probe(k, h, 1)
        return h

    def _linear_probe(self, k, h, step):
        """ Returns an index pointing to either an empty position or one that
        contains the tuple with the key
        """
        h += step
        index = h % len(self.l)
        if self.l[index] is None or self.l[index][0] == k:
            return index
        else:
            return self._linear_probe(k, h, step)

class LLNode:
    def __init__(self, e):
        self.element = e
        self.next = None
    def __str__(self):
        return str(self.element)

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        if not hasattr(head, 'next'): self.head = None

    def reverse(self):
        def _rec(prevnode, curnode):
            if curnode.next: _rec(curnode, curnode.next)
            else: self.head = curnode
            curnode.next = prevnode
        _rec(None, self.head)

    def find(self, e):
        def _rec(curnode):
            if not curnode or curnode.element == e:
                return curnode
            return _rec(curnode.next)
        return _rec(self.head)

    def delete(self, e):
        def _rec(curnode, prevnode, count):
            if not curnode:
                return count
            if curnode.element == e:
                count += 1
                if not prevnode:
                    self.head = curnode.next
                    return _rec(curnode.next, None, count)
                else:
                    prevnode.next = curnode.next
                    return _rec(curnode.next, prevnode, count)
            else: 
                return _rec(curnode.next, curnode, count)

        return _rec(self.head, None, 0)

    def tail(self):
        def _search(curnode):
            if curnode.next is None:
                return curnode
            return _search(curnode.next)

        if not self.head:
            return None
        return _search(self.head)

    def add(self, e):
        if not self.head:
            self.head = LLNode(e)
        else:
            self.tail().next = LLNode(e)

    def __str__(self):
        s = '['
        curnode = self.head
        while curnode:
            s += '{}, '.format(curnode.element)
            curnode = curnode.next
        s = s[:-2] + ']'
        return s



