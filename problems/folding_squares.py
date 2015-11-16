import sys
import math

def fold_left(strip):
    """
    size: 4
    0  1  2  3
          1  0

    0  1  2  3  4  5  6  7
    """
    if len(strip) % 2:
        print("can't fold in half")
        return

    middle = int(len(strip) / 2)
    new_strip = strip[middle:]
    for i in range(middle):
        index = -(i + 1) % middle
        # print("index", index)
        while strip[i]:
            new_strip[index].append(strip[i].pop())

    # first half of strip should be empty so return second half of strip
    return new_strip

def fold_right(strip):
    if len(strip) % 2:
        print("can't fold in half")
        return
    middle = int(len(strip) / 2)
    new_strip = strip[middle:]
    for i in range(middle):
        index = -(i + 1) % middle
        # print("index", index)
        while new_strip[index]:
            strip[i].append(new_strip[index].pop())
        new_strip[index] = strip[i]

    return list(reversed(new_strip))

def run(n):
    """ Given a strip of paper with 2^n squares, fold it in half from either the
    left or right side. Repeat until you have a single stack of squares and give
    the ordering of the numbers (bottom to top -> left to right on list)
    """
    strip = []
    for i in range(2**n):
        strip.append([i])

    # TODO loop for user input to fold either left or right and print after each

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("COMMAND: python3 {} <number>".format(sys.argv[0]))
    else:
        run(int(sys.argv[1]))