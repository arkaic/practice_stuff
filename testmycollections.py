import unittest, mycollections, random

class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.ht = mycollections.HashtableOA()
        krange = 1000
        num_elements = 1000
        for i in range(num_elements):
            k = random.randrange(krange)
            self.ht.put(k, i)

    def test_counts(self):
        manualcount = self._count_size(self.ht)
        self.assertEqual(self.ht.count, manualcount)

    def test_getput(self):
        k, v = 752, 7521
        self.assertNotEqual(self.ht.get(k), v)
        self.ht.put(k, v)
        self.assertEqual(self.ht.get(k), v)

    def _count_size(self, ht):
        c = 0
        for x in ht.l:
            if x is not None: c += 1
        return c

if __name__ == '__main__':
    unittest.main()