import math, unittest

class KitayutaMart2:
    def numBought(self, K, T):
        return math.log2(int(T / K) + 1)

class TestKitayutaMart2(unittest.TestCase):
    def test_numBought(self):
        inputs = []
        inputs.append([100, 100, 1])
        inputs.append([100, 300, 2])
        inputs.append([150, 1050, 3])
        inputs.append([160, 163680, 10])
        km = KitayutaMart2()
        for K, T, answer in inputs:
            self.assertEqual(km.numBought(K, T), answer)


if __name__ == '__main__':
    unittest.main()
