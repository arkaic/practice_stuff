import unittest, random
from datastructs import trees


class TestTrees(unittest.TestCase):

    def setUp(self):
        #       8
        #      / \
        #     3   10
        #    / \    \  
        #   1   6    14
        #      / \   /
        #     4   7 13

        self.bst = trees.BinarySearchTree(
            [None, 
             trees.Node(8, 1), 
             trees.Node(3, 2), 
             trees.Node(10, 3), 
             trees.Node(1, 4), 
             trees.Node(6, 5),
             None, 
             trees.Node(14, 7), 
             None,
             None, 
             trees.Node(4, 10),
             trees.Node(7, 11),
             None,
             None,
             trees.Node(13, 14),
             None]
        )
    
    def test_search(self):
        # todo search an empty tree too
        self.assertTrue(self.bst.search(8))
        self.assertTrue(self.bst.search(3))
        self.assertTrue(self.bst.search(10))
        self.assertTrue(self.bst.search(1))
        self.assertTrue(self.bst.search(6))
        self.assertTrue(self.bst.search(14))
        self.assertTrue(self.bst.search(4))
        self.assertTrue(self.bst.search(7))
        self.assertTrue(self.bst.search(13))
        self.assertFalse(self.bst.search(55))

if __name__ == '__main__':
    unittest.main()