import unittest

LUCKYS = {4,7,44,47,74,77,444,447,474}

class LuckyGrid:
    """https://community.topcoder.com/stat?c=problem_statement&pm=13894
    constraint is n <= 68
    """
    def findMinimumSum(self, grid):
        print(self._combo_nums(grid))

    def _combo_nums(self, grid):
        combo_nums = []
        n = len(grid)
        n = 8
        for i in range(n + 1):
            lucky = (4 * (n - i)) + (7 * i)
            if lucky > 474:
                break
            if  lucky in LUCKYS:
                combo_nums.append((n - i, i))
        return combo_nums


class TestLuckyGrid(unittest.TestCase):
    def setUp(self):
        self.lg = LuckyGrid()
        self.inputs = []
        self.inputs.append([["........",
                             "........",
                             "........",
                             "........",
                             "........",
                             "........",
                             "........",
                             "........"], 352])

        self.inputs.append([["."], 4])
        self.inputs.append([["7"], 7])
        self.inputs.append([[".4.",
                             "7.7",
                             "4.."], -1])
        # self.inputs.append([[
        #     ], 352])
        # self.inputs.append([[
            # ], 352])

    def test__combo_nums(self):
        for grid, answer in self.inputs:
            for f, s in self.lg._combo_nums(grid):
                self.assertTrue((4 * f + 7 * s) in LUCKYS)


if __name__ == '__main__':
    unittest.main()

    # def test__permute_combos(self):
    #     lg = LuckyGrid()
        # grid = ["........",
        #         "........",
        #         "........",
        #         "........",
        #         "........",
        #         "........",
        #         "........",
        #         "........"]
    #     permutes = []
    #     lg._permute_combos(0, permutes, 11)
    #     print('length of permutes={}'.format(len(permutes)))
    #     for permute in permutes:
    #         print(permute)
    #         self.assertTrue(sum(permute) in LUCKYS)