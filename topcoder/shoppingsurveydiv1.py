import unittest

class ShoppingSurveyDiv1:
    """https://community.topcoder.com/stat?c=problem_statement&pm=13455"""

    def minValue(self, n, k, S):
        # n = number of people
        # k = minimum items bought to be a Big Shopper
        # S = list of counts of each item
        # k cannot be more than the number of distinct items

        min_bigshoppers = 0
        while True:
            S = list(map(lambda x: x - 1, S))
            min_bigshoppers += 1
            # if i can divide the rest of items to everyone else and not 
            # come up with another big shopper, return min shoppers
            sum_remainingitems = sum(list(filter(lambda x: x >= 0, S)))
            d = int(sum_remainingitems / (n - min_bigshoppers))
            r = sum_remainingitems % (n - min_bigshoppers)
            if d == 0:
                return min_bigshoppers
            if d < k and r <= 1:
                return min_bigshoppers + r


class TestShoppingSurveyDiv1(unittest.TestCase):
    def test_minValue(self):
        inputs = []
        inputs.append([5, 2, [1,2,3], 1])
        inputs.append([4, 4, [4,4,4,2], 2])
        inputs.append([20, 3, [1, 10, 3, 4, 8, 15, 3, 16, 18, 2, 7, 3], 10])
        inputs.append([4, 2, [1, 2, 1, 1, 3, 1, 2, 2, 1, 2, 1], 2])
        inputs.append([2, 3, [1, 1, 1, 2], 1])

        ssd = ShoppingSurveyDiv1()
        for n, k, S, answer in inputs:
            self.assertEqual(ssd.minValue(n, k, S), answer)

if __name__ == '__main__':
    unittest.main()