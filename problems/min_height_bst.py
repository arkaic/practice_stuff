"""
    Problem: Given a sorted (increasing order) array, write an algorithm to create
    a binary tree with minimal height.
"""
import os
import random
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datastructs.trees import BinaryNode
from datastructs.trees import BinarySearchTree

TEST_ARRAYS = [
    ([33], 0),
    ([23, 89, 100, 200], 2),
    ([1,2,3,7,23,29,36,57,63,67,72,99], 3),
    ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 3),
    ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 4),
    (sorted(random.sample(range(100), 32)), 5),  # randomly generate list, no dupes
    (sorted(random.sample(range(100), 64)), 6),
]

def solve_it(arr, bst):
    if len(arr) == 1:
        assert bst.insert(BinaryNode(arr.pop()))  # assert that insertion works
    elif len(arr) > 1:
        middle = int(len(arr) / 2)
        left_half = arr[:middle]
        right_half = arr[middle:]
        assert bst.insert(BinaryNode(right_half.pop(0)))

        solve_it(left_half, bst)
        solve_it(right_half, bst)

if __name__ == '__main__':
    for test_array, expected_height in TEST_ARRAYS:
        # print(test_array)
        array_length = len(test_array)

        test_bst = BinarySearchTree()
        solve_it(test_array, test_bst)

        assert array_length == test_bst.count, 'array length={}\nbst length={}'.format(array_length, test_bst.count)
        # print(test_bst)
        assert expected_height == test_bst.height, 'Expected height = {}\nActual height = {}'.format(expected_height, test_bst.height)
    
    print('Tests pass')