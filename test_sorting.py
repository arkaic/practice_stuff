import unittest, random
from  unittest import TestCase
from datastructs import sorting

SAMPLESIZE = 100
NUM_RANDOM = 500

QS = 0
MS = 1
IS = 2
SS = 3

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
        self._trialtesting(QS)

    def test_mergesort(self):
        self._trialtesting(MS)

    def test_selectsort(self):
        self._trialtesting(SS)

    def test_insertionsort(self):
        self._trialtesting(IS)

    def _trialtesting(self, sort_type):
        for i in range(SAMPLESIZE):
            if not self.ready:
                self.setUp()

            unsorted_count = len(self.l)
            if sort_type == QS:
                sorted_l = sorting.quicksort_inplace(self.l, 0, unsorted_count - 1)
            elif sort_type == MS:
                sorted_l = sorting.mergesort(self.l)
            elif sort_type == IS:
                sorted_l = sorting.insertionsort(self.l)
            elif sort_type == SS:
                sorted_l = sorting.selectsort(self.l)
            self.assertEqual(unsorted_count, len(sorted_l))

            # Assert sorted list is in ascending order
            prev = -1
            for x in sorted_l:
                self.assertGreaterEqual(x, prev)
                prev = x

            # Assert that the elements were all accounted for from dictionary
            for x in sorted_l:
                self.assertTrue(x in self.d)
                self.d[x] -= 1
                self.assertGreaterEqual(self.d[x], 0)
            for k, v in self.d.items():
                self.assertEqual(v, 0)

            self.tearDown()

if __name__ == '__main__':
    unittest.main()
