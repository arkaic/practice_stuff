import unittest, random
from datastructs import trees

LEFT_SUBTREE = 0
RIGHT_SUBTREE = 1

ROOTS_LEFT_ANOMALIES = [8]
ROOTS_RIGHT_ANOMALIES = [3, 10]

class TestTrees(unittest.TestCase):

    def setUp(self):
        def _generate_connected_nodes(els):
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


        #       8
        #     /   \
        #    3     10
        #  /  \   /  \  
        # 1    6      14
        #/ \  / \    /
        #     4  7  13
        #    [2][9] [9]

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
        nodes = _generate_connected_nodes(els)
        wrong_nodes = _generate_connected_nodes(wrong_els)
        single_node = _generate_connected_nodes(single_el)

        # Create the bsts (wrongbst breaks the property of bsts)
        self.bst = trees.BinarySearchTree(root=nodes[1])
        self.bst.count = 9
        self.wrongbst = trees.BinarySearchTree(root=wrong_nodes[1])
        self.wrongbst.count = 9
        self.singlebst = trees.BinarySearchTree(root=single_node[1])
        self.singlebst.count = 1

    
    def test_search(self):
        # test that roots can also be searched for in a single element bst
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

    def test_insert(self):
        self.assertFalse(self.singlebst.insert(trees.Node(8)))
        self.assertTrue(self.singlebst.insert(trees.Node(1)))
        self.assertEqual(self.singlebst.count, 2)

        self.assertEqual(self.bst.count, 9)
        self.assertTrue(self.bst.insert(trees.Node(0)))
        self.assertTrue(self.bst.insert(trees.Node(-1)))
        self.assertTrue(self.bst.insert(trees.Node(17)))
        self.assertFalse(self.bst.insert(trees.Node(0)))
        self.assertFalse(self.bst.insert(trees.Node(-1)))
        self.assertFalse(self.bst.insert(trees.Node(1)))
        self.assertFalse(self.bst.insert(trees.Node(8)))
        self.assertFalse(self.bst.insert(trees.Node(3)))
        self.assertFalse(self.bst.insert(trees.Node(10)))
        self.assertFalse(self.bst.insert(trees.Node(1)))
        self.assertFalse(self.bst.insert(trees.Node(6)))
        self.assertFalse(self.bst.insert(trees.Node(14)))
        self.assertFalse(self.bst.insert(trees.Node(4)))
        self.assertFalse(self.bst.insert(trees.Node(7)))
        self.assertFalse(self.bst.insert(trees.Node(13)))
        self.assertTrue(self.bst.insert(trees.Node(55)))
        self.assertEqual(self.bst.count, 13)

    def test_bstproperty(self):
        """ All children of a node's left subtree must be less than, and vice versa. """

        def _dfs_all(node):
            """dfs_all() will recursively go through all nodes.
            dfs_subtree() will recursively go through all nodes of each dfs_all's node's
            subtree and check that every number holds true to the bst property.
            """
            def _dfs_subtree(subtreenode, el, subtree):
                if subtreenode:
                    if subtree == LEFT_SUBTREE:
                        self.assertLess(subtreenode.element, el)
                    elif subtree == RIGHT_SUBTREE:
                        self.assertLess(el, subtreenode.element)
                    _dfs_subtree(subtreenode.left, el, subtree)
                    _dfs_subtree(subtreenode.right, el, subtree)

            if node:
                _dfs_subtree(node.left, node.element, LEFT_SUBTREE)
                _dfs_subtree(node.right, node.element, RIGHT_SUBTREE)
                _dfs_all(node.left)
                _dfs_all(node.right)
                # self.bst.count -= 1


        _dfs_all(self.bst.root)

        # Assert that after each insert and delete, property still holds
        self.bst.insert(trees.Node(9))
        _dfs_all(self.bst.root)
        self.bst.delete(9)
        _dfs_all(self.bst.root)
        self.bst.insert(trees.Node(2))
        _dfs_all(self.bst.root)
        self.bst.delete(2)
        _dfs_all(self.bst.root)
        self.bst.insert(trees.Node(5))
        _dfs_all(self.bst.root)
        self.bst.delete(5)
        _dfs_all(self.bst.root)

        # Delete non existent element
        self.bst.delete(99)
        _dfs_all(self.bst.root)

        # Delete preexisting then reinsert
        self.bst.delete(8)
        _dfs_all(self.bst.root)
        self.bst.insert(trees.Node(8))
        _dfs_all(self.bst.root)
        self.bst.delete(7)
        _dfs_all(self.bst.root)
        self.bst.insert(trees.Node(7))
        _dfs_all(self.bst.root)

        # self.assertEqual(self.bst.count, 0)  # hack to see if dfs was looking through everything
        # _dfs_all(self.wrongbst.root)   # this will assert false


if __name__ == '__main__':
    unittest.main()

