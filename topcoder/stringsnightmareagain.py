import unittest

class StringsNightmareAgain:
    """ https://community.topcoder.com/stat?c=problem_statement&pm=12916 """
    def UniqueSubstrings(self, a, b, c, d, n):
        # make string list
        l = ['a'] * n
        for i in range(a):
            b = (b * c + d) % n
            l[b] = 'b'
        # print('STRING = {}'.format(''.join(l)))

        count = 0
        checked = set()
        for i in range(1, int(n / 2) + 1):
            # iterating over size of magical
            a_count = b_count = 0
            if i == 1:
                # for singular characters, we're just looking for a's and b's
                s = set()
                for c in l:
                    s.add(c)
                    if len(s) == 2: break
                count += len(s)
            else:
                j = 0
                while j + (i * 2) <= n:
                    # iterating over string with current size
                    start, end = j, j + i
                    j += 1
                    magical = ''.join(l[start:end])
                    if magical in checked:
                        continue
                    checked.add(magical)

                    k = end
                    while k + i <= n:
                        against = ''.join(l[k: k + i])
                        if against == magical:
                            count += 1
                            break
                        k += 1
        return count


class TestSNA(unittest.TestCase):
    def test_UniqueSubstrings(self):
        inputs = []
        inputs.append([0,0,0,0,4,2])
        inputs.append([2,3,1,1,6,3])
        inputs.append([4,3,1,1,6,3])
        inputs.append([4,3,3,3,10,5])
        inputs.append([5,3,2,3,11,9])
        inputs.append([10,1000000,1000000,1,51,63])
        sna = StringsNightmareAgain()
        for a, b, c, d, n, answer in inputs:
            self.assertEqual(sna.UniqueSubstrings(a, b, c, d, n), answer)


if __name__ == '__main__':
    unittest.main()