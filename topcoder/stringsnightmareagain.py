import unittest

class StringsNightmareAgain:
    """ https://community.topcoder.com/stat?c=problem_statement&pm=12916 """
    def UniqueSubstrings(self, a, b, c, d, n):
        # make string list
        l = ['a'] * n
        for i in range(a):
            b = (b * c + d) % n
            l[b] = 'b'
        print('STRING = {}'.format(''.join(l)))

        count = 0
        checked = set()
        for i in range(1, int(n / 2) + 1):
            # iterating over size of magical
            if i == 1:
                checked.add('a')
                if len(list(filter(lambda x: x == 'a', l))) > 1:
                    count += 1
                checked.add('b')
                if len(list(filter(lambda x: x == 'b', l))) > 1:
                    count += 1
            else:
                for j in range(n):
                    # iterating over string with current size

                    # break out if the current magical exceeds n
                    if (j + (i * 2)) > n: break

                    magical = ''.join(l[j: j + i])
                    if magical in checked:
                        continue
                    checked.add(magical)

                    k = j + i
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