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

class LinkedList(unittest.TestCase):

    def setUp(self):
        self.elements = [1,99,8,2,3,6,7]
        self.nodes = []
        prev = None
        for e in self.elements:
            n = mycollections.LLNode(e)
            self.nodes.append(n)
            if prev:
                prev.next = n
            prev = n
        self.assertEqual(len(self.elements), len(self.nodes))
        for i,n in enumerate(self.nodes):
            if i != len(self.nodes) - 1:
                self.assertNotEqual(n.next, None)

        self.ll = mycollections.LinkedList(self.nodes[0])

    def test_reverse(self):
        # TODO put asserts
        print('Test reverse')
        print('BEFORE REVERSE: {}'.format(self.ll))
        self.assertTrue(self.ll.head is self.nodes[0])
        self.ll.reverse()
        print('AFTER REVERSE:  {}'.format(self.ll))
        self.assertTrue(self.ll.head is self.nodes[len(self.nodes) - 1])


if __name__ == '__main__':
    unittest.main()