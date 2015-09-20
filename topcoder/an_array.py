import unittest
"""
http://community.topcoder.com/stat?c=problem_statement&pm=13994

Constraints
  A contains between 3 and 2000 elements, inclusive
  each element between 1 and 100 mil
  K -> [1, 1mil]
"""

class AnArray:
    def solveProblem(self, A, k):
        """ Given a int[] A with N elements and an int K, count the number of 
        tuples (p, q, r) such that 0 <= p < q < r < N and A[p] * A[q] * A[r] is
        divisible by K.
        """
        count = 0
        for p in range(0, len(A)):
            for q in range(p + 1, len(A)):
                for r in range(q + 1, len(A)):
                    if A[p] * A[q] * A[r] % k == 0: count += 1
        return count


class TestAnArray(unittest.TestCase):
    def setUp(self):
        self.inputs = []
        self.inputs.append(([31, 1, 3, 7, 2, 5], 30, 1))
        self.inputs.append(([4, 5, 2, 25], 100, 2))
        self.inputs.append(([100000000, 100000000, 100000000], 1000000, 1))
        self.inputs.append(([269, 154, 94, 221, 171, 154, 50, 210, 258, 358, 121, 159, 8, 47, 290, 125, 291, 293, 338, 248, 295, 160, 268, 227, 99, 4, 273], 360, 114))
        self.inputs.append(([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 220))
        self.anarray = AnArray()

    def test_solveproblem(self):
        for A, K, answer in self.inputs:
            self.assertEqual(self.anarray.solveProblem(A, K), answer, "A={}, K={}".format(A, K))

if __name__ == '__main__':
    unittest.main()