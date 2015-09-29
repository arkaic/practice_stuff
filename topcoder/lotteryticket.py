import unittest

class LotteryTicket:
    """https://community.topcoder.com/stat?c=problem_statement&pm=10860"""

    def buy(self, price, b1, b2, b3, b4):
        # Utilize recursive knapsack. Instead of finding max, knapsack
        # will just check if c can ever equal price. The returns are then
        # OR'd so that a single True means it's possible
        def _knapsack(bs, i, c):
            if c == price:
                return True
            if c > price or i >= len(bs):
                return False
            return _knapsack(bs, i + 1, c + bs[i]) or _knapsack(bs, i + 1, c)

        if _knapsack([b4, b3, b1, b2], 0, 0):
            return 'POSSIBLE'
        else: 
            return 'IMPOSSIBLE'

        
class TestLotteryTicket(unittest.TestCase):
    def test_buy(self):
        inputs = []
        inputs.append([10, 1, 5, 10, 50, "POSSIBLE"])
        inputs.append([15, 1, 5, 10, 50, "POSSIBLE"])
        inputs.append([65, 1, 5, 10, 50, "POSSIBLE"])
        inputs.append([66, 1, 5, 10, 50, 'POSSIBLE'])
        inputs.append([1000, 999, 998, 997, 996, "IMPOSSIBLE"])
        inputs.append([20, 5, 5, 5, 5, "POSSIBLE"])
        inputs.append([2, 1, 5, 10, 50, "IMPOSSIBLE"])
        lt = LotteryTicket()
        for price, b1, b2, b3, b4, answer in inputs:
            self.assertEqual(lt.buy(price, b1, b2, b3, b4), answer)


if __name__ == '__main__':
    unittest.main()