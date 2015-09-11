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

        # Test case elements. 
        els = [None, 8, 
               3, 10, 
               1, 6, None, 14, 
               None, None, 4, 7, None, None, 13, None]
        wrong_els = [None, 8, 
                     3, 10, 
                     1, 6, None, 14, 
                     None, None, 2, 9, None, None, 9, None]
        single_el = [None, 8]

        # Generate a linked tree of Node objects
        nodes = self._generate_connected_nodes(els)
        wrong_nodes = self._generate_connected_nodes(wrong_els)
        single_node = self._generate_connected_nodes(single_el)

        # Create the bsts (wrongbst breaks the property of bsts)
        self.bst = trees.BinarySearchTree(root=nodes[1])
        self.bst.count = 9
        self.wrongbst = trees.BinarySearchTree(root=wrong_nodes[1])
        self.wrongbst.count = 9
        self.singlebst = trees.BinarySearchTree(root=single_node[1])
        self.singlebst.count = 1

    
    def test_search(self):
        self.assertEqual(self.singlebst.search(8).element, 8)
        self.assertEqual(self.singlebst.search(4), None)

        self.assertEqual(self.bst.search(8).element, 8)
        self.assertEqual(self.bst.search(3).element, 3)
        self.assertEqual(self.bst.search(10).element, 10)
        self.assertEqual(self.bst.search(1).element, 1)
        self.assertEqual(self.bst.search(6).element, 6)
        self.assertEqual(self.bst.search(14).element, 14)
        self.assertEqual(self.bst.search(4).element, 4)
        self.assertEqual(self.bst.search(7).element, 7)
        self.assertEqual(self.bst.search(13).element, 13)
        self.assertEqual(self.bst.search(55), None)

    # def test_insert(self):
        self.assertFalse(self.singlebst.insert(8))
        self.assertTrue(self.singlebst.insert(1))
        self.assertEqual(self.singlebst.count, 2)

        self.assertEqual(self.bst.count, 9)
        self.assertTrue(self.bst.insert(0))
        self.assertTrue(self.bst.insert(-1))
        self.assertTrue(self.bst.insert(17))
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
        self.assertEqual(self.bst.count, 13)

    # def test_bstproperty(self):
    #     for i in range(1, len(self.bst.l)):
    #         node = self.bst.l[i]
    #         if node:
    #             left, right = i * 2, i * 2 + 1
    #             self.assertTrue(self._check_subtree(left, node, LESSTHAN, self.bst))
    #             self.assertTrue(self._check_subtree(right, node, GREATERTHAN, self.bst))

    #     for i in range(1, len(self.wrongbst.l)):
    #         node = self.wrongbst.l[i]
    #         if node:
    #             left, right = i * 2, i * 2 + 1
    #             if node.element in ROOTS_LEFT_ANOMALIES:
    #                 self.assertFalse(self._check_subtree(left, node, LESSTHAN, self.wrongbst))
    #             else:
    #                 self.assertTrue(self._check_subtree(left, node, LESSTHAN, self.wrongbst))

    #             if node.element in ROOTS_RIGHT_ANOMALIES:
    #                 self.assertFalse(self._check_subtree(right, node, GREATERTHAN, self.wrongbst))
    #             else:
    #                 self.assertTrue(self._check_subtree(right, node, GREATERTHAN, self.wrongbst))

    # def _check_subtree(self, desc, root, comparetype, tree):
    #     if desc < len(tree.l) and tree.l[desc] is not None:
    #         if comparetype == LESSTHAN and tree.l[desc].element >= root.element:
    #             return False
    #         elif comparetype == GREATERTHAN and tree.l[desc].element <= root.element:
    #             return False

    #         left, right = desc * 2, desc * 2 + 1
    #         if not self._check_subtree(left, root, comparetype, tree):
    #             return False
    #         if not self._check_subtree(right, root, comparetype, tree):
    #             return False

    #     return True

    def _generate_connected_nodes(self, els):
        nodes = []
        for x in els:
            if x is None: nodes.append(x)
            else: nodes.append(trees.Node(x))
        for i, node in enumerate(nodes):
            if node is not None:
                if i > 1: node.parent = nodes[int(i / 2)]
                if i * 2 < len(nodes): node.left = nodes[i * 2]
                if i * 2 + 1 < len(nodes): node.right = nodes[i * 2 + 1]
        return nodes

if __name__ == '__main__':
    unittest.main()
