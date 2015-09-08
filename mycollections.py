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
        elif self.l[h][0] == k:
            return self.l[h][1]
        else:
            h = self._linear_probe(k, h, 1)
            if self.l[h]:
                return self.l[h][1]
            return self.l[h]

    def put(self, k, v):
        h = self._hashfunc(k)
        if self.l[h] is None or self.l[h][0] == k:
            if self.l[h] is None:
                self.count += 1
            self.l[h] = (k, v)
        else:
            # linear probing method
            index = self._linear_probe(k, h, 1)
            if self.l[index] is None:
                self.count += 1
            self.l[index] = (k, v)

        if self.count > .7 * len(self.l):
            # resize
            self.count = 0
            old_l = self.l
            self.l = [None] * (len(old_l) * 2)
            for x in old_l:
                if x is not None:
                    self.put(x[0], x[1])

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

    def remove(self, k):
        hash = index = self._hashfunc(k)
        step = 1
        while self.l[index] is not None and self.l[index][0] != k:
            hash += step
            index = hash % len(self.l)

        pair = self.l[index]
        if self.l[index] is not None:
            self.l[index] = None
            self.count -= 1
        return pair

    def _hashfunc(self, k):
        """ m <= size of array """
        a = 0.67
        m = len(self.l)  # prime
        return floor(m * (k * a - floor(k * a)))

################################################################################


def main(args):
    k_range = args.krange
    h = HashtableOA()
    for i in range(1000):
        k = randrange(k_range)
        h.put(k, i)
    print(h.l)

if __name__ == '__main__':
    pass
    # parser = argparse.ArgumentParser()
    # parser.add_argument('krange', help='k range')
    # args = parser.parse_args()
    # main(args)
