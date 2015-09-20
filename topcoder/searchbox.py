""" http://community.topcoder.com/stat?c=problem_statement&pm=8019 """

import unittest

class SearchBox:
    def find(self, text, search, wholeWord, start):
        for i in range(start, len(text)):
            if text[i] == search[0]:
                t, s = i, 0
                is_match = False
                while t < len(text) and text[t] == search[s]:
                    s, t = s + 1, t + 1
                    if s == len(search):
                        if wholeWord == 'N':
                            return i
                        elif wholeWord == 'Y':
                            if i == 0 or text[i - 1] == ' ':
                                if t == len(text) or text[t] == ' ': return i
                            break
        return -1


class TestSearchBox(unittest.TestCase):
    def setUp(self):
        self.inputs = []
        self.inputs.append(('We dont need no education', 'ed', 'N', 13, 16))
        self.inputs.append(("We dont need no thought control", 'We', 'Y', 0, 0))
        self.inputs.append(("No dark sarcasm in the classroom", 'The', 'Y', 5, -1))
        self.inputs.append(("Teachers leave them kids alone", 'kid', 'Y', 1, -1))
        self.inputs.append(("All in all its just another brick in the wall", 'all', 'Y', 9, -1))
        self.inputs.append(("All in all youre just another brick in the wall", 'just', 'Y', 17, 17))
        self.sb = SearchBox()

    def test_find(self):
        for text, search, wholeWord, start, answer in self.inputs:
            self.assertEqual(self.sb.find(text, search, wholeWord, start), 
                             answer,
                             "{} {} {} {} {}".format(text, search, wholeWord, start, answer))

if __name__ == '__main__':
    unittest.main()