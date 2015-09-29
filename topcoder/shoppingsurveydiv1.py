import unittest

class ShoppingSurveyDiv1:
    """https://community.topcoder.com/stat?c=problem_statement&pm=13455"""

    def minValue(self, n, k, S):
        # n = number of people
        # k = minimum items bought to be a Big Shopper
        # S = list of counts of each item
        # k <= size of S

        # Strategy: first, take a shopper and assume he buys one of each item
        # in S, automatically making him a big shopper. Divide the sum of
        # the rest of the items amongst the rest of the shoppers.
        # If there are more buyers than the sum, then there're no more big 
        # shoppers. If the dividing allocates an amount ONE less than k to everyon
        # else AND there are none left over, then there are no more big shoppers.
        # If there is one left over, then there is one more big shopper as she
        # buys this extra item bumping her to having bought k items. 
        # If the quotient is less than k-1, there's also obviously no more big 
        # shoppers
        min_bigshoppers = 0
        while True:
            S = list(map(lambda x: x - 1, S))
            min_bigshoppers += 1
            sum_remainingitems = sum(list(filter(lambda x: x >= 0, S)))
            quo = int(sum_remainingitems / (n - min_bigshoppers))
            rem = sum_remainingitems % (n - min_bigshoppers)
            if quo == k - 1 and rem <= 1:
                return min_bigshoppers + rem
            elif quo < k - 1:
                return min_bigshoppers


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
