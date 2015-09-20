"""
https://leetcode.com/problems/text-justification/
"""

class Solution(object):
    def fullJustify(self, words, maxWidth):
        for word in words:
            if len(word) > maxWidth:
                raise Exception('word is longer than maxwidth')

        # build list of word lists for each line
        lines = [[]]
        char_count = 0  # count of chars without spaces
        for i, word in enumerate(words):
            num_spaceslots = len(lines[len(lines) - 1]) - 1
            a = char_count + num_spaceslots + 1 + len(word)
            if char_count + num_spaceslots + 1 + len(word) <= maxWidth:
                lines[len(lines) - 1].append(word)
                char_count += len(word)
            else:
                lines.append([])
                char_count = len(word)
                lines[len(lines) - 1].append(word)

        # create correctly justified strings for each line in lines
        justified = []
        for line in lines:
            char_count = sum([len(w) for w in line])
            num_justified_spaces = maxWidth - char_count
            if len(line) == 1:
                justified.append(line[0] + ' ' * num_justified_spaces)
            else:
                num_spaceslots = len(line) - 1
                per_spaceslot = int(num_justified_spaces / num_spaceslots)
                rem = num_justified_spaces % num_spaceslots
                just_word = ''
                for i, w in enumerate(line):
                    if i == 0:
                        just_word += w
                    else:
                        # evenly distribute extra spaces from the left
                        if rem:
                            just_word += ' ' * (per_spaceslot+1) + w
                            rem -= 1
                        else:
                            just_word += ' ' * per_spaceslot + w
                justified.append(just_word)
            print("")
        return justified

if __name__ == '__main__':
    words = ["This", "is", "a", "sick", "example", "of", 'a', "textual", "justification."]
    l = 16
    s = Solution().fullJustify(words, l)
    for x in s:
        print('"{}"'.format(x))