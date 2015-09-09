import unittest, random
from  unittest import TestCase
from datastructs import sorting

class TestQuicksort(TestCase):

    def setUp(self):
        r = 1000
        self.l = [random.randrange(100) for x in range(r)]
        self.d = dict()
        for x in self.l:
            if x not in self.d:
                self.d[x] = 0
            self.d[x] += 1

    def test_qsinplace(self):
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


if __name__ == '__main__':
    unittest.main()
