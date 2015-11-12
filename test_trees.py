import unittest, random, math
from datastructs import trees

LEFT_SUBTREE = 0
RIGHT_SUBTREE = 1

BST = 2
RBT = 3

ROOTS_LEFT_ANOMALIES = [8]
ROOTS_RIGHT_ANOMALIES = [3, 10]

SAMPLE_SIZE = 100

B, R = trees.BLACK, trees.RED

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        def _generate_connected_nodes(els, treetype):
            nodes = []
            for i, x in enumerate(els):
                if x is None:
                    nodes.append(x)
                else:
                    nodes.append(trees.Node(x))

            # connect them
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
        self.bst_elements = [None, 8, 
               3, 10, 
               1, 6, 9, 14, 
               None, None, 4, 7, None, None, 13, None]
        self.wrongbst_elements = [None, 8, 
                     3, 10, 
                     1, 6, None, 14, 
                     None, None, 2, 9, None, None, 9, None]
        self.singlebst_element = [None, 8]

        # Generate a linked tree of Node objects
        nodes = _generate_connected_nodes(self.bst_elements, BST)
        wrong_nodes = _generate_connected_nodes(self.wrongbst_elements, BST)
        single_node = _generate_connected_nodes(self.singlebst_element, BST)

        # Create the bsts (wrongbst breaks the property of bsts)
        self.bst = trees.BinarySearchTree(root=nodes[1])
        self.bst.count = 9
        self.wrongbst = trees.BinarySearchTree(root=wrong_nodes[1])
        self.wrongbst.count = 9
        self.singlebst = trees.BinarySearchTree(root=single_node[1])
        self.singlebst.count = 1
    
    def test_search(self):
        print("\n********TEST B.S. TREE SEARCH PROPERTIES*******")
        # test that roots can also be searched for in a single element bst
        self.assertEqual(self.singlebst.search(8).element, 8)
        self.assertEqual(self.singlebst.search(4), None)

        for e in self.bst_elements:
            if e is not None: 
                self.assertEqual(self.bst.search(e).element, e)

    def test_insert(self):
        print("\n********TEST B.S. TREE INSERT PROPERTIES*******")
        self.assertFalse(self.singlebst.insert(trees.Node(8)))
        self.assertTrue(self.singlebst.insert(trees.Node(1)))
        self.assertEqual(self.singlebst.count, 2)

        self.assertEqual(self.bst.count, 9)
        self.assertTrue(self.bst.insert(trees.Node(0)))
        self.assertTrue(self.bst.insert(trees.Node(-1)))
        self.assertTrue(self.bst.insert(trees.Node(17)))
        self.assertTrue(self.bst.insert(trees.Node(55)))
        self.assertFalse(self.bst.insert(trees.Node(0)))
        self.assertFalse(self.bst.insert(trees.Node(-1)))

        for e in self.bst_elements:
            if e is not None:
                self.assertFalse(self.bst.insert(trees.Node(e)))

        self.assertEqual(self.bst.count, 13)

    def test_bstproperty(self):
        """ All children of a node's left subtree must be less than, and vice versa. """
        print("\n********TEST B.S. TREE PROPERTIES*******")

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
                if node.left:
                    print("stn={}, topel={}".format(node.left.element, node.element))
                _dfs_subtree(node.left, node.element, LEFT_SUBTREE)
                _dfs_subtree(node.right, node.element, RIGHT_SUBTREE)
                _dfs_all(node.left)
                _dfs_all(node.right)
                # self.bst.count -= 1


        _dfs_all(self.bst.root)

        # Assert that after each insert and delete, property still holds
        els = [9, 2, 5]
        for e in els:
            self.bst.insert(trees.Node(e))
            _dfs_all(self.bst.root)
            self.bst.delete(e)
            _dfs_all(self.bst.root)

        # Delete non existent element
        self.bst.delete(99)
        _dfs_all(self.bst.root)

        # Delete preexisting then reinsert
        els = [8, 7, 14, 1, 4]
        for e in els:
            print(self.bst)
            print("deleting {}".format(e))
            self.bst.delete(e)
            print(self.bst)
            _dfs_all(self.bst.root)
            self.bst.insert(trees.Node(e))
            _dfs_all(self.bst.root)

        # self.assertEqual(self.bst.count, 0)  # hack to see if dfs was looking through everything
        # _dfs_all(self.wrongbst.root)   # this will assert false

    def test_bstdelete(self):
        print("\n********TEST B.S. TREE DELETE*******")
        elements = [3, 7, 10]
        print(self.bst)
        for e in elements:
            node, replacement = self.bst.delete(e)
            # print(node.element, "for", replacement.element)
            print(self.bst)
            if replacement:
                self.assertTrue(self.bst.search(replacement.element) is not None, e)


class TestRedBlackTree(unittest.TestCase):

    def setUp(self):
        # END

        #       11
        #     /   \
        #    2R    14
        #  /  \   /  \  
        # 1   7     15R
        #/ \ / \    / \
        #    5R 8R

        # redblack elements. Because tree is binary, I need the first elemen 
        # to be None so I can easily assign children/parents to nodes in
        # the nested function above
        rb_els = [None, (11,B),
                  (2, R), (14, B),
                  (1, B), (7, B), None, (15, R),
                  None, None, (5, R), (8, R), None, None, None, None]

        # Generate a linked tree of Node objects
        rbnodes = self._generate_connected_nodes(rb_els, RBT)
        # wrong_rbnodes = self._generate_connected_nodes(self.wrongbst_elements, RBT)

        # Create the RBTs (wrong RBTs break the property of RBTs)
        self.rbt = trees.RedBlackTree(root=rbnodes[1])
        self.rbt.count = 9
        self.initial_bh_rbt = 2
        self.measured_bh = None
        # self.wrongrbt = trees.RedBlackTree(root=wrong_rbnodes[1])
        # self.wrongrbt.count = 9

    def test_rbtproperty(self):
        """ Root is black, black depth is equal from every leaf,
        all red parents have black children
        """
        print("\n********TEST REDBLACKTREE PROPERTIES*******")
        
        # assert root is black
        self.assertEqual(self.rbt.root.color, trees.BLACK)
        
        if self.rbt.root: 
            self._dfs_test_rbt_property(self.rbt.root)

        # TODO do insertions and deletions and then check the bh
        elements_toinsert = [4, 3, 13, 6, 40, 20, 30]
        elements_toinsert = [4]
        for e in elements_toinsert:
            self.measured_bh = None
            self.rbt.insert(trees.RedBlackNode(e, trees.RED))
            self._dfs_test_rbt_property(self.rbt.root)

        # Insert numbers larger than rbt max until black height reaches threshold
        i = 50
        while self.measured_bh < 8:
            self.measured_bh = None
            i += 1
            self.rbt.insert(trees.RedBlackNode(i, trees.RED))
            self._dfs_test_rbt_property(self.rbt.root)

        # Get actual height of rbt by traversing it, preferring right children
        height = 0
        ptr = self.rbt.root
        while ptr:
            height += 1
            if ptr.right: ptr = ptr.right
            elif ptr.left: ptr = ptr.left
            else: ptr = None
        print('Height after long insertions: {}'.format(height))
        # assert that black height is >= to half the actual height rounded up
        self.assertGreaterEqual(self.measured_bh, math.ceil(height/2))

        for i in range(SAMPLE_SIZE):
            self.measured_bh = None
            r = random.randrange(0, 100)
            self.rbt.insert(trees.RedBlackNode(r, trees.RED))
            self._dfs_test_rbt_property(self.rbt.root)

    def test_rbtdelete(self):
        print("\n********TEST REDBLACKTREE DELETE********")
        # todo make a new tree to test all possible cases of deletion

        print(self.rbt)

        # self.rbt.delete(8)
        self.rbt.delete(7)
        # self.rbt.delete(2)

        self._dfs_test_rbt_property(self.rbt.root)


    def _dfs_test_rbt_property(self, node):
        """ A recursive function that tests redblack tree property for a given 
        node and recursively its children. Utilizes two nested recursive 
        functions for this task
        """

        def _black_height(n):
            """ recursively finds black height of a leaf """
            if n.color == trees.BLACK:
                if n.parent:
                    return 1 + _black_height(n.parent)
                else: 
                    return 1
            if n.parent: 
                return _black_height(n.parent)
            else: 
                return 0

        def _black_height_to_leaves(n):
            """ Recursively checks if black heights to all of n's leaves are
            the same. For any recursive call, it returns either the black 
            height, or -1 if it finds that the node's children have 
            mismatching black heights
            """
            if not n.left and not n.right:
                if n.color == B: return 1
                else: return 0
            
            leftsum = rightsum = 0
            if n.left:
                # recurse for resulting sum
                leftsum = _black_height_to_leaves(n.left)
            if n.right:
                rightsum = _black_height_to_leaves(n.right)

            if leftsum != rightsum or leftsum == -1 or rightsum == -1:
                return -1
            else:
                # when both children's bh's are equal, pass this up, depending
                # on the current node's color
                if n.color == B:
                    return 1 + leftsum
                else:
                    return leftsum

        # DFS nodes down to leaves, then call _black_height on leaf
        if not node.left and not node.right:
            # assert black height of leaf
            bh = _black_height(node)
            if self.measured_bh is None: 
                self.measured_bh = bh
            self.assertEqual(bh, self.measured_bh)
        else:
            # assert properties of each node
            # assert that each node has the same black height to ANY of its
            # desendent leaves
            if node.color == trees.RED:
                if node.left: 
                    self.assertEqual(node.left.color, trees.BLACK)
                if node.right:
                    self.assertEqual(node.right.color, trees.BLACK)
                self.assertTrue(node is not self.rbt.root) # can't be a root
                self.assertNotEqual(node.parent, None)  # roots have no parent
                self.assertEqual(node.parent.color, trees.BLACK)

            self.assertNotEqual(_black_height_to_leaves(node), -1)

            # recurse down to each child
            if node.left: 
                self._dfs_test_rbt_property(node.left)
            if node.right: 
                self._dfs_test_rbt_property(node.right)

    def _generate_connected_nodes(self, els, treetype):
        nodes = []
        for i, x in enumerate(els):
            if x is None: nodes.append(x)
            else: nodes.append(trees.RedBlackNode(x[0], x[1]))

        # connect them
        for i, node in enumerate(nodes):
            if node is not None:
                if i > 1: node.parent = nodes[int(i / 2)]
                if i * 2 < len(nodes): node.left = nodes[i * 2]
                if i * 2 + 1 < len(nodes): node.right = nodes[i * 2 + 1]
        return nodes


if __name__ == '__main__':
    unittest.main()
    # u = TestRedBlackTree()
    # u.setUp()
    # u.test_rbtdelete()

