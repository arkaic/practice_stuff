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
        hash = index = self._hashfunc(k)
        step = 1
        while self.l[index] is not None and self.l[index][0] != k:
            hash += step
            index = hash % len(self.l)

        if self.l[index] is None:
            return None
        else:
            return self.l[index][1]

    def put(self, k, v):
        hash = self._hashfunc(k)
        if self.l[hash] is None:
            self.l[hash] = (k, v)
            self.count += 1
        else:
            # linear probing method
            probe = self._linear_probe(k, hash, 1)
            if self.l[probe] is None:
                self.count += 1
            self.l[probe] = (k, v)

        if self.count > .7 * len(self.l):
            # resize
            self.count = 0
            old_l = self.l
            self.l = [None] * (len(old_l) * 2)
            for x in old_l:
                if x is not None:
                    self.put(x[0], x[1])

    def remove(self, k):
        # TODO
        pass

    def _linear_probe(self, k, hash, step):
        probe = (hash + step) % len(self.l)
        if self.l[probe] is None or self.l[probe][0] == k:
            return probe
        else:
            return self._linear_probe(k, hash + 1, step)

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

    k,v = 752, 7521

    print("Getting {} ====> {}".format(k, h.get(k)))

    print("Putting {},{}".format(k, v))
    h.put(k, v)

    print("Getting {} ====> {}".format(k, h.get(k)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('krange', help='k range')
    args = parser.parse_args()
    main(args)
