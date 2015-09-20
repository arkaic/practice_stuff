"""
http://community.topcoder.com/stat?c=problem_statement&pm=13744
"""

import unittest

class DevuAndGame:
    def canWin(self, nextLevel):
        history = set()
        current = nextLevel[0]
        # If you revisit a location, then there is a loop
        while current not in history:
            if current == -1:
                return 'Win'
            history.add(current)
            current = nextLevel[current]
        return 'Lose'


class TestDevuAndGame(unittest.TestCase):
    def setUp(self):
        self.inputs = []
        self.inputs.append(([1, -1], 'Win'))
        self.inputs.append(([1, 0, -1], 'Lose'))
        self.inputs.append(([0, 1, 2], 'Lose'))
        self.inputs.append(([29,33,28,16,-1,11,10,14,6,31,7,35,34,8,15,17,26,12,13,22,1,20,2,21,-1,5,19,9,18,4,25,32,3,30,23,10,27], 'Win'))
        self.inputs.append(([17,43,20,41,42,15,18,35,-1,31,7,33,23,33,-1,-1,0,33,19,12,42,-1,-1,9,9,-1,39,-1,31,46,-1,20,44,41,-1,-1,12,-1,36,-1,-1,6,47,10,2,4,1,29], 'Win'))
        self.inputs.append(([3, 1, 1, 2, -1, 4], 'Lose'))
        self.dag = DevuAndGame()

    def test_canWin(self):
        for nextLevel, answer in self.inputs:
            self.assertEqual(self.dag.canWin(nextLevel), answer, "{}".format(nextLevel))


if __name__ == '__main__':
    unittest.main()