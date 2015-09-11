import unittest, random
from datastructs import trees

LESSTHAN = 0
GREATERTHAN = 1

ROOTS_LEFT_ANOMALIES = [8]
ROOTS_RIGHT_ANOMALIES = [3, 10]

class TestTrees(unittest.TestCase):

    def setUp(self):
        #       8
        #     /   \
        #    3     10
        #  /  \   /  \  
        # 1    6      14
        #/ \  / \    /
        #     4  7  13

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
        
        self.wrongbst = trees.BinarySearchTree(
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
             trees.Node(2, 10),
             trees.Node(9, 11),
             None,
             None,
             trees.Node(9, 14),
             None]
        )

        self.assertFalse(self.bst is self.wrongbst)
    
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

    def test_insert(self):
        original_list_size = len(self.bst.l)
        self.assertTrue(self.bst.insert(0))
        self.assertEqual(original_list_size, len(self.bst.l))
        self.assertTrue(self.bst.insert(-1))
        self.assertEqual(original_list_size * 2, len(self.bst.l))
        self.assertTrue(self.bst.insert(17))
        self.assertEqual(original_list_size * 2, len(self.bst.l))
        self.assertFalse(self.bst.insert(0))
        self.assertFalse(self.bst.insert(-1))
        self.assertFalse(self.bst.insert(1))
        self.assertFalse(self.bst.insert(8))
        self.assertFalse(self.bst.insert(3))
        self.assertFalse(self.bst.insert(10))
        self.assertFalse(self.bst.insert(1))
        self.assertFalse(self.bst.insert(6))
        self.assertFalse(self.bst.insert(14))
        self.assertFalse(self.bst.insert(4))
        self.assertFalse(self.bst.insert(7))
        self.assertFalse(self.bst.insert(13))
        self.assertTrue(self.bst.insert(55))

    def test_bstproperty(self):
        # todo should make trees that break property
        for i in range(1, len(self.bst.l)):
            node = self.bst.l[i]
            if node:
                left, right = i * 2, i * 2 + 1
                self.assertTrue(self._check_subtree(left, node, LESSTHAN, self.bst))
                self.assertTrue(self._check_subtree(right, node, GREATERTHAN, self.bst))

        for i in range(1, len(self.wrongbst.l)):
            node = self.wrongbst.l[i]
            if node:
                left, right = i * 2, i * 2 + 1
                if node.element in ROOTS_LEFT_ANOMALIES:
                    self.assertFalse(self._check_subtree(left, node, LESSTHAN, self.wrongbst))
                else:
                    self.assertTrue(self._check_subtree(left, node, LESSTHAN, self.wrongbst))

                if node.element in ROOTS_RIGHT_ANOMALIES:
                    self.assertFalse(self._check_subtree(right, node, GREATERTHAN, self.wrongbst))
                else:
                    self.assertTrue(self._check_subtree(right, node, GREATERTHAN, self.wrongbst))

    def _check_subtree(self, desc, root, comparetype, tree):
        if desc < len(tree.l) and tree.l[desc] is not None:
            if comparetype == LESSTHAN and tree.l[desc].element >= root.element:
                return False
            elif comparetype == GREATERTHAN and tree.l[desc].element <= root.element:
                return False

            left, right = desc * 2, desc * 2 + 1
            if not self._check_subtree(left, root, comparetype, tree):
                return False
            if not self._check_subtree(right, root, comparetype, tree):
                return False

        return True

if __name__ == '__main__':
    unittest.main()
