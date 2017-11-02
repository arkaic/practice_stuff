#!/usr/bin/env python3
import sys

TEST_CASES = [
    (31, 14, 2),
    (21, 53, 1),     # 010101 vs 110101
    (89, 133, 5),    # 01011001 vs 10000101
    (1845, 777, 5),  # 11100110101 vs 01100001001
]

def bitcountdiffer(a, b):
    """
    Determine the number of bits required to convert integer a to integer b

    Args:
        a: integer
        b: integer
    
    Returns:
        integer, the count of bits that need to be flipped
    """
    # XOR for binary number with 1s for all bits that were different
    xord = a ^ b

    # count the 1s with this trick
    count = 0
    while xord > 0:
        count += 1
        # result will be 0 when xord is a power of two
        xord = xord & (xord - 1)
    return count

if __name__ == '__main__':
    if len(sys.argv) == 1:
        do_tests_even_pass = True
        for a, b, expected in TEST_CASES:
            count = bitcountdiffer(a, b)
            try:
                assert count == expected
            except AssertionError:
                do_tests_even_pass = False
                print('For {} and {}\nExpected: {}\nActual:   {}\n'.format(a, b, expected, count))
        if do_tests_even_pass:
            print('Tests pass')
        else:
            print('Tests are not passing')
    elif len(sys.argv) == 3:
        count = bitcountdiffer(int(sys.argv[1]), int(sys.argv[2]))
        print(str(count))
    else:
        exit('Nothing happened')