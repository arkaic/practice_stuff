import unittest

class ConcatenateNumbers:

    def numberOfSegments(self, L, R, v):
        def _f(x, y):
            return int(''.join(list(map(lambda z: str(z), range(x, y + 1)))))

        count = 0
        for x in range (L, R + 1):
            for y in range(x, R + 1):
                if _f(x, y) == v % 1000000007:
                    count += 1
        return count

class TestConcatNumbers(unittest.TestCase):
    def test_numberOfSegments(self):
        inputs = []
        inputs.append([11, 13, 111213, 1])
        inputs.append([11, 13, 11213, 0])
        inputs.append([11, 13, 14, 0])
        inputs.append([1, 100000, 12345, 10])
        inputs.append([999900001, 1000000000, 0, 7])
        cn = ConcatenateNumbers()
        for L, R, v, answer in inputs:
            self.assertEqual(cn.numberOfSegments(L, R, v), answer, 
                'L={}; R={}; v={}; ans={}'.format(L,R,v,answer))


if __name__ == '__main__':
    unittest.main()