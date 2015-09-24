import unittest

class EightRooks:
    """https://community.topcoder.com/stat?c=problem_statement&pm=13773"""

    def isCorrect(self, board):
        c = 0
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == 'R':
                    c += 1
                    for k in range(len(board)):
                        if k != i and board[k][j] == 'R':
                            return 'Incorrect'
                    for m in range(len(row)):
                        if m != j and board[i][m] == 'R':
                            return 'Incorrect'
                    if c == 8: break
            if c == 8: break
        if c < 8: 
            return 'Incorrect'
        else:
            return 'Correct'

class TestEightRooks(unittest.TestCase):
    def setUp(self):
        self.input = []
        self.input.append([["R.......",
                           ".R......",
                           "..R.....",
                           "...R....",
                           "....R...",
                           ".....R..",
                           "......R.",
                           ".......R"], 'Correct'])
        self.input.append([["........",
                           "....R...",
                           "........",
                           ".R......",
                           "........",
                           "........",
                           "..R.....",
                           "........"], 'Incorrect'])
        self.input.append([["......R.",
                           "....R...",
                           "...R....",
                           ".R......",
                           "R.......",
                           ".....R..",
                           "..R.....",
                           ".......R"], 'Correct'])
        self.input.append([["......R.",
                           "....R...",
                           "...R....",
                           ".R......",
                           "R.......",
                           ".......R",
                           "..R.....",
                           ".......R"], 'Incorrect'])
        self.input.append([["........",
                           "........",
                           "........",
                           "........",
                           "........",
                           "........",
                           "........",
                           "........"], 'Incorrect'])

    def test_isCorrect(self):
        er = EightRooks()
        c = 0
        for board, answer in self.input:
            self.assertEqual(er.isCorrect(board), answer, "c=" + str(c))
            c += 1


if __name__ == '__main__':
    unittest.main()