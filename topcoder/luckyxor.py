import unittest

class LuckyXor:
    """ https://community.topcoder.com/stat?c=problem_statement&pm=13960 
    CONSTRAINTS:  a is between 1-100 inclusive
    """

    def construct(self, a):
        def _xor(c, d):
            binc, bind = format(c, '#09b')[2:], format(d, '#09b')[2:]
            s = ""
            for i, digit in enumerate(binc):
                if digit == bind[i]:
                    s += '0'
                else:
                    s += '1'
            return int(s, 2)

        luckys = {4, 7, 44, 47, 74}
        if a < 1 or a > 100:
            raise Exception('invalid input')
        bs = set()
        for i in range(1, 101):            
            xor_result = _xor(a, i)
            if xor_result in luckys:
                bs.add(i)
        if bs: return bs
        else: return {-1}


class TestLuckyXor(unittest.TestCase):
    def setUp(self):
        self.inputs = []
        self.inputs.append([4, 40])
        self.inputs.append([19, 20])
        self.inputs.append([88, 92])
        self.lx = LuckyXor()

    def test_construct(self):
        for a, b in self.inputs:
            self.assertTrue(b in self.lx.construct(a), '{} xor something = {}'.format(a,self.lx.construct(a)))

if __name__ == '__main__':
    unittest.main()