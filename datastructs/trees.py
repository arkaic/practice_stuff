import math

BLACK = 0
RED = 1

class Node:
    def __init__(self, element, parent=None, left=None, right=None):
        self.element = element
        self.parent = parent
        self.left = left
        self.right = right


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
            if not node or el == node.element: 
                return node
            elif el < node.element: 
                return _dfs(node.left)
            else: 
                return _dfs(node.right)
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
        """ 
        Case 1: Node is leaf
        Case 2: Node has left child only
        Case 3: Node has right child only
        Case 4: Node has both children --> replace with smallest node in right
                subtree
        """
        node = self.search(el)

        if not node:
            return None

        replacement = None
        if not node.right:
            if not node.left:
                # Case 1: node is leaf
                if node.element > node.parent.element:
                    node.parent.right = None
                else:
                    node.parent.left = None
            else:
                # Case 2: node has left only
                node.left.parent = node.parent
                if node is node.parent.right:
                    node.parent.right = node.left
                elif node is node.parent.left:
                    node.parent.left = node.left
                else:
                    raise Exception("shouldn't happen")
                replacement = node.left
        elif not node.left:
            # Case 3: node has right only
            node.right.parent = node.parent
            if node is node.parent.right:
                node.parent.right = node.right
            elif node is node.parent.left:
                node.parent.left = node.right
            else:
                raise Exception("shouldn't happen")
            replacement = node.right
        else:
            # Case 4 
            if not node.right.left:
                # just use deleted node's right child as replacement
                replacement = node.right
                replacement.left = node.left
                replacement.parent = node.parent
                replacement.left.parent = replacement
                if node.parent:
                    if node.parent.left == node:
                        node.parent.left = replacement
                    elif node.parent.right == node:
                        node.parent.right = replacement
                    else: 
                        raise Exception("shouldn't happen")
            else:
                # Get smallest node in right subtree for replacement
                replacement = node.right
                while replacement.left:
                    replacement = replacement.left

                # update references of old neighbors of replacement
                replacement.parent.left = replacement.right
                if replacement.right:
                    replacement.right.parent = replacement.parent

                # update replacement's refs
                replacement.left = node.left
                replacement.right = node.right
                replacement.parent = node.parent

                # update replacement's new left's and right's parent refs
                replacement.left.parent = replacement
                replacement.right.parent = replacement

                # update deleted node's parent's child ref to replacement
                if node == node.parent.left:
                    node.parent.left = replacement
                elif node == node.parent.right:
                    node.parent.right = replacement
                else: 
                    raise Exception("shouldn't happen")

            if replacement.parent is None:
                self.root = replacement

        node.right = None
        node.left = None
        node.parent = None
        self.count -= 1

        return (node, replacement)

    def __str__(self):
        c = 0 
        level = 1
        q = [self.root]
        s = "--------------------------\nP ---> N(L, R)\n"
        while q:
            n = q.pop(0)
            if n:
                c += 1
                if n.parent:
                    el_str = 'P={} ---> {}('.format(n.parent.element, n.element)
                else:
                    el_str = 'P=NIL ---> {}('.format(n.element)
                if n.left: el_str += '{}, '.format(n.left.element)
                else: el_str += 'NIL, '
                if n.right: el_str += '{})'.format(n.right.element)
                else: el_str += 'NIL)'
                q.append(n.left)
                q.append(n.right)
            else:
                el_str = 'NIL'
            s += el_str + '\n'
        s += '\nNode Count sans NILs = {}\n--------------------------'.format(c)
        return s


class RedBlackNode(Node):
    """ Red/Black Notes
    Properties: 
      1. root property: Black root
      2. red property: RED nodes have BLACK children
      3. black property: Leaves are BLACK (None), and all have same black depth

    Left Rotation: 
    x=parent, y=right child. y lets go left, pulls its right up and above x, and y
    connects to x as its new left, connecting x's older parent to itself. At the 
    same time, x disconnects y (its right), drops down to connect to y's old left

      p              p
     /              /
    x              y
     \      --->  / \
      y          x   R
     / \          \
    L   R          L

    left child -> right_rotate
    right child -> left_rotate
    """
    def __init__(self, element, color, parent=None, left=None, right=None):
        super().__init__(element, parent, left, right)
        self.color = color


class RedBlackTree(BinarySearchTree):
    """ NIL leaves are None """

    def __init__(self, root=None):
        super().__init__(root)

    # @Override
    def insert(self, node):
        """ All nodes are inserted as red, except if the node is the first
        node added in for the tree """
        if not hasattr(node, 'color'):
            # could make this more robust?
            raise AttributeError("Node provided is not a RedBlackNode")

        if self.count == 0: node.color = BLACK
        else: node.color = RED
        if super().insert(node):
            self._balance(node)

    # @Override 
    def delete(self, el):
        """ 
        Case 1: deleted node is leaf
        Case 2: deleted node has only left
        Case 3: deleted node has only right
        Balance bh starting at the substituted node if deleted node is black.

        Case 4: deleted node has both children
        if red deleted and subbed with red, nothing needed
        if red deleted and subbed with black, balance at subtree (red property)
        if black deleted and subbed with black, balance starting at the subtree
        if black deleted and subbed with red, balance at substituted node
        """

        nodes = super().delete(el)
        if not nodes: 
            return None
        deleted, replacement = nodes

        if replacement:
            replacement.color = RED
            # TODO (unfinished?)
            self._balance(replacement)

    def _balance(self, x):
        """ The rotations here are called either with the current x OR with its 
        grandparent """
        # Could find another way to retrieve element's node
        if x is not self.search(x.element):
            raise Exception("Not supposed to happen")

        # Node x will be constantly reassigned, thus this while loop.
        # loop continues until current node doesn't break red property
        while x is not self.root and x.color == RED and x.parent.color == RED:
            if not x.parent.parent:
                raise Exception("Test exception: root is red and is x's parent" + 
                    "in this iteration of rb algorithm")

            # x.parent's color is RED, so it will never be a root. Thus, x has 
            # a grandparent, and why there is no null check here for the gp
            if x.parent is x.parent.parent.left:
                # x's parent is a left child
                uncle = x.parent.parent.right
                if not uncle or uncle.color == BLACK:
                    if x is x.parent.right:
                        x = x.parent
                        self._left_rotate(x)
                    x.parent.color = BLACK
                    x.parent.parent.color = RED
                    self._right_rotate(x.parent.parent)  # gives x a red parent
                else:
                    # uncle exists and it's red, so we're just going to make both
                    # parent and uncle black and grandparent red. Reassign x to gp
                    x.parent.color = BLACK
                    uncle.color = BLACK
                    x.parent.parent.color = RED
                    x = x.parent.parent
                    if x.parent is None:
                        self.root = x
            elif x.parent is x.parent.parent.right:
                # above with left/right switched
                uncle = x.parent.parent.left
                if not uncle or uncle.color == BLACK:
                    # uncle may be NIL or he is black
                    if x is x.parent.left:
                        # if x is left child
                        x = x.parent
                        self._right_rotate(x)
                    x.parent.color = BLACK
                    x.parent.parent.color = RED
                    self._left_rotate(x.parent.parent)
                else:
                    # uncle exists and color is red
                    x.parent.color = BLACK
                    uncle.color = BLACK
                    x.parent.parent.color = RED
                    x = x.parent.parent
                    if x.parent is None:
                        self.root = x

        self.root.color = BLACK

    def _left_rotate(self, x):
        """ x = parent; y = right child """
        y = x.right
        if x.parent:
            if x.parent.left is x: x.parent.left = y
            elif x.parent.right is x: x.parent.right = y
            else: raise Exception('Not supposed to happen')
        else:
            self.root = y

        y.parent = x.parent

        if y.left: y.left.parent = x

        x.parent = y
        x.right = y.left

        y.left = x

    def _right_rotate(self, x):
        """ x = parent; y = left child """
        y = x.left
        if x.parent:
            if x.parent.right is x: x.parent.right = y
            elif x.parent.left is x: x.parent.left = y
            else: raise Exception('Not supposed to happen')
        else:
            self.root = y

        y.parent = x.parent

        if y.right: y.right.parent = x

        x.parent = y
        x.left = y.right

        y.right = x
