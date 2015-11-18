import sys
import math

def fold_right(strip):
    """ The left side of the strip is folded over the right """
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

def fold_left(strip):
    """ The right side of the strip is folded over the left """
    if len(strip) % 2:
        print("can't fold in half")
        return

    middle = int(len(strip) / 2)
    new_strip = strip[middle:]
    for i in range(middle):
        index = -(i + 1) % middle
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

    while len(strip) > 1:
        print(strip)
        fold_direction = input("Fold direction? [l/r/q] -> ")
        if fold_direction.lower() == 'l':
            strip = fold_left(strip)
        elif fold_direction.lower() == 'r':
            strip = fold_right(strip)
        elif fold_direction.lower() == 'q':
            print("quitting")
            return
        else:
            print("Invalid input")

    print("\nFINAL\n", strip)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("FOLDING SQUARES")
        print("A program that folds a strip of paper with numbered 2^n squares in",
              "halves depending on which direction you choose to fold in each time",
              "and outputs the order of the squares.")
        print("COMMAND: python3 {} <number>".format(sys.argv[0]))
    else:
        run(int(sys.argv[1]))