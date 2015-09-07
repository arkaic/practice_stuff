class HashtableOA:
    """ Open addressing method """

    _init_size = 97
    l = None
    count = None

    def __init__(self):
        self.l = [None] * self._init_size
        self.count = 0

    def put(self, k, v):
        hash = self._hashfunc(k)
        if self.l[hash] is None:
            self.l[hash] = (k, v)
        else:
            # linear probing method
            probe = self._linear_probe(hash, 1)
            if self.l[probe] is None:
                self.l[probe] = (k, v)

        self.count += 1        
        if self.count > .7 * len(self.l):
            # resize
            self.count = 0
            old_l = self.l
            self.l = [None] * (len(old_l) * 2)
            for x in old_l:
                if x is not None:
                    self.put(x[0], x[1])
                

    def _linear_probe(self, hash, step):
        probe = (hash + step) % len(self.l)
        if self.l[probe] is None:
            return probe
        else:
            return self._linear_probe(hash + 1, step)

    def _hashfunc(self, k):
        """ m <= size of array """
        a = 0.67
        m = len(self.l)  # prime
        return floor(m * (k * a - floor(k * a)))


################################################################################
import sys
from math import floor
from random import randrange

if __name__ == '__main__':
    k_range = 97
    if len(sys.argv) == 2:
        k_range = int(sys.argv[1])
    h = HashtableOA()
    for i in range(1000):
        k = randrange(k_range)
        h.put(k, i)
    print(h.l)