import unittest, random
from datastructs import mycollections

class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.ht = mycollections.HashtableOA()
        krange = 1000
        num_elements = 1000
        self.k = random.randrange(krange)
        self.v = random.randrange(10000)
        for i in range(num_elements):
            k = random.randrange(krange)
            self.ht.put(k, i)

    def test_counts(self):
        manualcount = self._count_size(self.ht)
        self.assertEqual(self.ht.count, manualcount)

    def test_getput(self):
        ht = self.ht
        k, v = self.k, self.v
        self.assertNotEqual(ht.get(k), v)
        b = ht.put(k, v)
        self.assertEqual(ht.get(k), v)

    def test_remove(self):
        ht = self.ht
        k, v = self.k, self.v
        self.assertEqual(ht.count, self._count_size(ht))
        b = ht.put(k, v)
        self.assertEqual(ht.count, self._count_size(ht))
        self.assertEqual(ht.get(k), v)
        pair = ht.remove(k)
        self.assertEqual(ht.count, self._count_size(ht))
        self.assertEqual(pair[0], k)
        self.assertEqual(pair[1], v)
        self.assertEqual(ht.get(k), None)

    def _count_size(self, ht):
        c = 0
        for x in ht.l:
            if x is not None: c += 1
        return c

if __name__ == '__main__':
    unittest.main()