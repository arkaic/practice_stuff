# Given an NxN matrix, rotate it 90 degrees IN PLACE 

import unittest


CLOCKWISE = 0
COUNTERCLOCKWISE = 1


def transpose(matrix):
    """ in place transpose """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp
    return matrix

def rotate(matrix, dir):
    """ in place rotation """
    matrix = transpose(matrix)
    if dir == CLOCKWISE:
        # reverse each row
        for row in matrix:
            for i in range(len(row)):
                left, right = i, len(row) - 1 - i
                if left >= right: 
                    break
                else:
                    tmp = row[left]
                    row[left] = row[right]
                    row[right] = tmp
    elif dir == COUNTERCLOCKWISE:
        # reverse row order
        for i, row in enumerate(matrix):
            top, bottom = i, len(matrix) - 1 - i
            if top >= bottom:
                break
            else:
                tmp = matrix[top]
                matrix[top] = matrix[bottom]
                matrix[bottom] = tmp
    return matrix


class TestRotate(unittest.TestCase):
    def setUp(self):
        self.inputs = []
        self.inputs.append([
            [[4,3,5],
             [6,7,9],
             [9,2,3]],
            [[4,6,9],
             [3,7,2],
             [5,9,3]],
            [[9,6,4],
             [2,7,3],
             [3,9,5]],
            [[5,9,3],
             [3,7,2],
             [4,6,9]]])
        self.inputs.append([
            [[4,3,5,6],
             [6,7,9,7],
             [9,2,3,8],
             [5,2,4,1]],
            [[4,6,9,5],
             [3,7,2,2],
             [5,9,3,4],
             [6,7,8,1]],
            [[5,9,6,4],
             [2,2,7,3],
             [4,3,9,5],
             [1,8,7,6]],
            [[6,7,8,1],
             [5,9,3,4],
             [3,7,2,2],
             [4,6,9,5]]])

    # for tests below, assert that the in place operations produce both 
    # intended AND inplace results
    def test_transpose(self):
        for matrix, transposed, cwmatrix, ccwmatrix in self.inputs:
            trans_matrix = transpose(matrix)
            self.assertTrue(trans_matrix is matrix)
            self.assertEqual(trans_matrix, transposed)

    def test_rotate_clockwise(self):
        for matrix, transposed, cwmatrix, ccwmatrix in self.inputs:
            rotatedtmp = rotate(matrix, CLOCKWISE)
            self.assertTrue(rotatedtmp is matrix)
            self.assertTrue(rotatedtmp == cwmatrix)

    def test_rotate_counterclockwise(self):
        for matrix, transposed, cwmatrix, ccwmatrix in self.inputs:
            rotatedtmp = rotate(matrix, COUNTERCLOCKWISE)
            self.assertTrue(rotatedtmp is matrix)
            self.assertTrue(rotatedtmp == ccwmatrix)

if __name__ == '__main__':
    unittest.main()