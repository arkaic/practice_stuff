import unittest, random
from  unittest import TestCase
from datastructs import sorting

SAMPLESIZE = 100
NUM_RANDOM = 500

class TestSorting(TestCase):

    def setUp(self):
        self.ready = True
        self.l = [random.randrange(100) for x in range(NUM_RANDOM)]
        self.d = dict()
        for x in self.l:
            if x not in self.d:
                self.d[x] = 0
            self.d[x] += 1
        self.assertEqual(NUM_RANDOM, len(self.l))

    def tearDown(self):
        self.ready = False
        self.l = None
        self.d = None

    def test_qsinplace(self):
        for i in range(SAMPLESIZE):
            if not self.ready: self.setUp()

            # Assert that sorted list has same amount of items
            unsorted_count = len(self.l)
            sorting.quicksort_inplace(self.l, 0, unsorted_count - 1)
            self.assertEqual(unsorted_count, len(self.l))

            # Assert each subsequent item >= previous item
            prev = -1
            for x in self.l:
                self.assertGreaterEqual(x, prev)
                prev = x

            # Assert each sorted item was noted in dictionary, then decrement
            for x in self.l:
                self.assertTrue(x in self.d)
                self.d[x] -= 1
                self.assertGreaterEqual(self.d[x], 0)

            # Assert dictionary is empty and all zeroed out
            for k, v in self.d.items():
                self.assertEqual(v, 0)

            self.tearDown()

    def test_mergesort(self):
        for i in range(SAMPLESIZE):
            if not self.ready: self.setUp()

            sorted_l = sorting.mergesort(self.l)
            self.assertEqual(len(sorted_l), len(self.l))

            prev = -1
            for x in sorted_l:
                self.assertGreaterEqual(x, prev)
                prev = x

            for x in sorted_l:
                self.assertTrue(x in self.d)
                self.d[x] -= 1
                self.assertGreaterEqual(self.d[x], 0)
 
            for k, v in self.d.items():
                self.assertEqual(v, 0)

            self.tearDown()

    def test_selectsort(self):
        for i in range(SAMPLESIZE):
            if not self.ready: 
                self.setUp()

            sorted_l = sorting.selectsort(self.l)
            self.assertEqual(len(sorted_l), NUM_RANDOM)

            prev = -1
            for x in sorted_l:
                self.assertGreaterEqual(x, prev)
                prev = x

            for x in sorted_l:
                self.assertTrue(x in self.d)
                self.d[x] -= 1
                self.assertGreaterEqual(self.d[x], 0)
 
            for k, v in self.d.items():
                self.assertEqual(v, 0)

            self.tearDown()


if __name__ == '__main__':
    unittest.main()
