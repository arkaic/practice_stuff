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
        self.element_not_included = 7521
        self.elements = [1,99,8,2,3,6,7,2]
        self.elements_no_dupes = [1,99,8,2,3,6,7]
        self.nodes = []
        self.nodes_no_dupes = []
        prev = None
        for e in self.elements:
            n = mycollections.LLNode(e)
            self.nodes.append(n)
            if prev:
                prev.next = n
            prev = n
        self.assertEqual(len(self.elements), len(self.nodes))

        prev = None
        for e in self.elements_no_dupes:
            n = mycollections.LLNode(e)
            self.nodes_no_dupes.append(n)
            if prev:
                prev.next = n
            prev = n
        self.assertEqual(len(self.elements_no_dupes), len(self.nodes_no_dupes))

        for i,n in enumerate(self.nodes):
            if i != len(self.nodes) - 1:
                self.assertNotEqual(n.next, None)

        self.ll = mycollections.LinkedList(self.nodes[0])
        self.ll_no_dupes = mycollections.LinkedList(self.nodes_no_dupes[0])

    def test_reverse(self):
        # TODO put asserts
        print('Test reverse')
        print('BEFORE REVERSE: {}'.format(self.ll))
        self.assertTrue(self.ll.head is self.nodes[0])
        self.ll.reverse()
        print('AFTER REVERSE:  {}'.format(self.ll))
        self.assertTrue(self.ll.head is self.nodes[len(self.nodes) - 1])

    def test_find(self):
        for i, e in enumerate(self.elements_no_dupes):
            print('i ' + str(i))
            print('e ' + str(e))
            print(self.nodes_no_dupes[i])
            self.assertTrue(self.ll_no_dupes.find(e) is self.nodes_no_dupes[i])
        self.assertTrue(self.ll_no_dupes.find(self.element_not_included) is None)

    def test_tail(self):
        self.assertTrue(self.ll.tail() is self.nodes[len(self.nodes) - 1])        
        self.assertTrue(self.ll_no_dupes.tail() is self.nodes_no_dupes[len(self.nodes_no_dupes) - 1])

    def test_add(self):
        added_element = 5
        self.ll.add(added_element)
        self.assertTrue(self.ll.tail().element == added_element)



    def test_delete(self):
        print('TEST DELETE')
        print('Before:    {}'.format(self.ll))
        self.ll.delete(2)
        print('AFter (2): {}'.format(self.ll))
        self.ll.delete(self.ll.head.element)
        self.assertTrue(self.ll.head is self.nodes[1])


if __name__ == '__main__':
    unittest.main()