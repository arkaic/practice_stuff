import unittest

class FoxCardGame:
    """ https://community.topcoder.com/stat?c=problem_statement&pm=11236 """
    def theMaxProportion(self, A, B, k):
        # Generate all possible pairs
        pairs = []
        for a in A:
            for b in B:
                pairs.append((a, b))

        self.divided = None
        self._recurse(pairs, k, 0, 0)
        return self.divided

    def _recurse(self, pairs, k, j, h):
        if k == 0:
            if self.divided is None: 
                self.divided = j / h
            else:
                self.divided = max(self.divided, j / h)
            return

        for a, b in pairs:
            # clone pairs with all tuples that have either/both a and b removed
            clone = list(filter(
                lambda x: x[0] != a and x[0] != b and x[1] != a and x[1] != b, 
                pairs
            ))
            self._recurse(clone, k - 1, j + max(a+b, a*b), h + min(a+b, a*b))


class TestFoxCardGame(unittest.TestCase):
    def test_theMaxProportion(self):
        inputs = []
        inputs.append([[1,2,3], [4,5,6], 2, 1.7692307692307692])
        inputs.append([[1.234, 5.678, 9.012, 3.456, 7.89], 
                       [2.345, 6.789, 9.876, 5.432, 1.012], 
                        3, 
                        4.159424420079523])
        inputs.append([[1, 1.1, 1.2, 1.3, 1.4, 1.5],
                       [5, 10, 15, 20, 25, 30],
                        2,
                        1.3972602739726028])
        inputs.append([[85.302, 92.798, 76.813, 37.994, 36.737, 98.659],
                       [13.352, 7.3094, 54.761, 8.2706, 63.223, 37.486],
                        3,
                        33.58603889836175])
        fcg = FoxCardGame()
        for A, B, k, answer in inputs:
            print('k={}, answer={}'.format(k, answer))
            self.assertEqual(round(fcg.theMaxProportion(A, B, k), 10), round(answer, 10))

if __name__ == '__main__':
    unittest.main()