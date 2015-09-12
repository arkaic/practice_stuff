BLACK = 0
RED = 1

class Node:
    def __init__(self, element, parent=None, left=None, right=None):
        self.element = element
        self.parent = parent
        self.left = left
        self.right = right


class RedBlackNode(Node):
    """ Red/Black Notes
    Properties: 
      1. Black root
      2. Leaves are None and considered Black, and all have same black depth
      3. Red's children are black

    Left Rotation: 
    x=parent, y=right child. y lets go left, pulls its right up and above x and
    connects to x as its new left, connecting x's older parent to itself. At the 
    same time, x disconnects y (its right), drops down to connect to y's old left

    left child -> right_rotate
    right child -> left_rotate

    Affected parties: x, y, x.parent, y.left
        if x.parent.left is x: x.parent.left = y
        elif: x.parent.right = y
        else: exception

        y.parent = x.parent

        y.left.parent = x

        x.parent = y
        x.right = y.left

        y.left = x
    """

    def __init__(self, element, color, parent=None, left=None, right=None):
        super().__init__(element, parent, left, right)
        self.color = color


class BinarySearchTree:

    def __init__(self, root=None):
        self.root = root
        self.count = 0
        self.last_added_node = None
        if root: 
            self.count += 1
            self.last_added_node = root
    
    def search(self, el):
        def _dfs(node):
            if not node or el == node.element: return node
            elif el < node.element: return _dfs(node.left)
            else: return _dfs(node.right)
        return _dfs(self.root)

    def insert(self, node):
        def _dfi(m):
            if node.element == m.element:
                return False  # already exists
            elif node.element < m.element:
                if m.left: 
                    return _dfi(m.left)
                else:
                    node.parent = m
                    m.left = node
                    self.last_added_node = node
            else:
                if m.right:
                    return _dfi(m.right)
                else:
                    node.parent = m
                    m.right = node
                    self.last_added_node = node
            self.count += 1
            return True

        if not self.root:
            self.root = node
            return True
        return _dfi(self.root)

    def delete(self, el):
        node = self.search(el)

        if not node:
            return False

        if not node.right:
            if not node.left:
                # leaf node
                if node.element > node.parent.element:
                    node.parent.right = None
                else:
                    node.parent.left = None
            else:
                # node just has left child
                node.left.parent = node.parent
                node.parent.left = node.left
        elif not node.left:
            # node has just right child
            node.right.parent = node.parent
            node.parent.right = node.right
        else:
            # node has both children
            # Get smallest node in right subtree
            subtree_node = node.right
            while subtree_node.left:
                subtree_node = subtree_node.left

            # connect subtree node's right child to subtree node's parent
            # substitute subtree node in place of the node to be deleted
            if subtree_node.right:
                subtree_node.right.parent = subtree_node.parent
                subtree_node.parent.left = subtree_node.right
            subtree_node.parent = node.parent
            subtree_node.left = node.left
            subtree_node.right = node.right

        node.right = None
        node.left = None
        node.parent = None
        self.count -= 1

        return True


class RedBlackTree(BinarySearchTree):

    def __init__(self, root=None):
        super().__init__(root)

    def insert(self, node):
        if not hasattr(node.color):
            # could make this more robust?
            raise AttributeError("Node provided is not a RedBlackNode")
        super().insert(node)

        x = self.last_added_node
        # Could find another way to retrieve el's node
        if x is not self.search(el):
            raise Exception("Not supposed to happen")

        while x is not self.root and x.parent.color == RED:
            if x.parent is self.root:
                raise Exception("Test exception: root is red and is x's parent in this iteration of rb algorithm")
            if x.parent.parent and x.parent is x.parent.parent.left:
                uncle = x.parent.parent.right
                if not uncle or uncle.color == BLACK:
                    # uncle may be NIL or he is black
                    if x is x.parent.right:
                        x = x.parent
                        self._left_rotate(x)
                    x.parent.color = BLACK
                    x.parent.parent.color = RED
                    self._right_rotate(x.parent.parent)  # gives x a red parent
                else:
                    # uncle exists and color is red
                    x.parent = BLACK
                    uncle.color = BLACK
                    x.parent.parent = RED
                    x = x.parent.parent
            elif x.parent.parent and x.parent is x.parent.parent.right:
                # above with left/right switched
                uncle = x.parent.parent.left
                if not uncle or uncle.color == BLACK:
                    # uncle may be NIL or he is black
                    if x is x.parent.left:
                        x = x.parent
                        self._right_rotate(x)
                    x.parent.color = BLACK
                    x.parent.parent.color = RED
                    self._left_rotate(x.parent.parent)
                else:
                    # uncle exists and color is red
                    x.parent = BLACK
                    uncle.color = BLACK
                    x.parent.parent = RED
                    x = x.parent.parent

        self.root.color = BLACK

    def _left_rotate(self):
        pass

    def _right_rotate(self):
        pass
