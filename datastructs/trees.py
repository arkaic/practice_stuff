BLACK = 0
RED = 1


################################################################################
#                            BINARY TREE                                       #
################################################################################


class BinaryNode:
    def __init__(self, element, parent=None, left=None, right=None):
        self.element = element
        self.parent = parent
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self, root=None):
        """
        Args:
            root - root BinaryNode
        """
        self.root = root
        self.count = 0
        self.last_added_node = None
        self.height = 0
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
        """
        Returns:
            True if insertion successful, False otherwise
        """
        if not self.root:
            assert self.height == 0
            self.root = node
            self.count += 1
            return True
        return self._dfi(self.root, node, 0)

    def _dfi(self, m, node, depth):
        """
        Recursively dfs and insert node into tree with m as parent

        Args:
            m     - BinaryNode representing our location
            node  - BinaryNode to insert
            depth - integer counter

        Returns:
            True if insertion made, False otherwise
        """
        if node.element == m.element:
            return False  # already exists
        elif node.element < m.element:
            if m.left:
                return self._dfi(m.left, node, depth + 1)
            else:
                node.parent = m
                m.left = node
                self.last_added_node = node
        else:
            if m.right:
                return self._dfi(m.right, node, depth + 1)
            else:
                node.parent = m
                m.right = node
                self.last_added_node = node

        # print('el=%s'%node.element)
        # print('depth=%s'%depth)
        self.height = max(self.height, depth + 1)
        self.count += 1
        return True

    def delete(self, el):
        """ 
        Case 1: Node is leaf
        Case 2: Node has left child only
        Case 3: Node has right child only
        Case 4: Node has both children --> replace with smallest node in right
                subtree
        TODO update self.height
        """
        node = self.search(el)

        if not node:
            return None

        deleted = None  # if node is internal, deleted is its replacement
        replacement = None  # if node is internal, replacement is replacement's repl
        parent_of_replacement = None  # keep track of the original parent of deleted
        rep_for_replacement = None
        if not node.right:
            deleted = node
            parent_of_replacement = node.parent

            if not deleted.left:
                # Case 1: delete-node is leaf          #(1,0,0)
                if deleted.element > deleted.parent.element:
                    deleted.parent.right = None
                else:
                    deleted.parent.left = None
            else:
                # Case 2: delete-node has left only    #(1,1,0)
                replacement = deleted.left
                replacement.parent = deleted.parent
                if deleted is deleted.parent.right:
                    deleted.parent.right = replacement
                elif deleted is deleted.parent.left:
                    deleted.parent.left = replacement
                else:
                    raise Exception("shouldn't happen")
        elif not node.left:
            # Case 3: node has right only       #(1,1,0)
            deleted = node
            parent_of_replacement = node.parent
            replacement = deleted.right

            replacement.parent = deleted.parent
            if deleted is deleted.parent.right:
                deleted.parent.right = replacement
            elif deleted is deleted.parent.left:
                deleted.parent.left = replacement
            else:
                raise Exception("shouldn't happen")
        else:
            # Case 4: Node is internal. Delete-node isn't actually deleted here, 
            # but moves to replace the internal node.
            deleted = node.right
            if not deleted.left:
                # replacement's parent won't change because we're using internal
                # node's right as its successor.
                replacement = deleted.right
                parent_of_replacement = deleted

                deleted.left = node.left
                deleted.parent = node.parent
                deleted.left.parent = deleted
            else:
                # Get smallest node in right subtree for replacement 
                while deleted.left:
                    deleted = deleted.left

                replacement = deleted.right
                parent_of_replacement = deleted.parent

                # update references of delete-node's old parent and replacement
                deleted.parent.left = replacement
                if replacement:
                    replacement.parent = deleted.parent

                # update delete-node's refs
                deleted.left = node.left
                deleted.right = node.right
                deleted.parent = node.parent

                # update delete-node's new children's parent refs
                deleted.left.parent = deleted
                deleted.right.parent = deleted

            # update internal node's parent's references to delete-node
            if deleted.parent:
                if node == deleted.parent.left:
                    deleted.parent.left = deleted
                elif node == deleted.parent.right:
                    deleted.parent.right = deleted
                else: 
                    raise Exception("shouldn't happen")
            else:
                self.root = deleted

        self.count -= 1
        return (deleted, replacement, parent_of_replacement)

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
        s += '\nNode Count sans NILs = {}'.format(c)
        s += '\nNode height = %s\n--------------------------' % self.height
        return s


################################################################################
#                           RED BLACK TREE                                     #
################################################################################


class RedBlackNode(BinaryNode):
    """ Red/Black Notes
    Properties: 
      1. root property: Black root
      2. red property: RED nodes have BLACK children
      3. black property: Leaves are BLACK (None), and all have same black depth
         a. From 3, can we say that red nodes CAN'T have one NON-NIL children?
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
    def delete(self, elem):
        """ 
        """

        try:
            # no change in time complexity at least
            original_delete_node_color = self.search(elem).color  
        except AttributeError:
            return None

        # Delete just like in a binary tree
        nodes = super().delete(elem)
        if not nodes: 
            return None
        # print(self)  # TODO delete this

        # unpack nodes involved in deletion
        deleted, replacement, replacements_parent = nodes

        # if delete-node is not the original node that was deleted, the original
        # node was an internal node. Change this delete-node to that internal's
        # original color. Save the original delete-node color too
        deleted_oldcolor = deleted.color
        if deleted.element != elem:
            deleted.color = original_delete_node_color

        # We can just consider cases where a leaf or a node with one child is
        # deleted. In the case where an internal node gets deleted, it just gets
        # replaced with its replacement, and then we have to consider deleting
        # THAT replacement. Since that replacement is the smallest node in the 
        # internal node's right child's subtree, the replacement will always be 
        # either a leaf or a node with just a right child. Thus, this third case 
        # reduces back to the first two cases.
        # ------------------------------------------------------------
 
        is_simple_case = False
        if (deleted_oldcolor is RED or 
                (replacement is not None and replacement.color is RED)):
            is_simple_case = True

        # Handle resultant cases
        if is_simple_case:
            print("HANDLE SIMPLE CASE FOR DELETE")
            if replacement: 
                replacement.color = BLACK
        else:
            print("HANDLE HARD CASE FOR DELETED:", elem)
            if replacement:
                raise Exception("shouldn't happen: replacement should be None" +
                    "right now but it is {}".format(replacement.element))
            if replacements_parent.left:    # TODO v coulda been root
                self._hard_case_for_delete(replacements_parent.left)
            else:
                self._hard_case_for_delete(replacements_parent.right)

    def _hard_case_for_delete(self, sibling):
        """ ...sibling to the replacement u
        while u is double black or it is not root:
        make u double black, even if it's NIL. 
        case a: sibling is black with red child (don't worry about double 
        blacking) base case
        case b: sibling is black leaf (this is recursive and has a basecase)
        case c: sibling is red with two children (this leads back to case 2's 
            basecase)
        """
        if not sibling: raise Exception("Shouldn't happen: sibling is empty")

        parent = sibling.parent
        if sibling.color is BLACK:
            if not sibling.left and not sibling.right:
                # case b - sibling is a leaf
                sibling.color = RED
                if sibling.parent.color is RED:
                    print(sibling.element)
                    sibling.parent.color = BLACK
                else:
                    if parent.parent:  # if not, parent is root and we are done
                        auntie = (parent.parent.right if parent.parent.left is parent
                                 else parent.parent.left)
                        self._hard_case_for_delete(auntie)
            else:
                # case a sibling is not a leaf and its children should be red
                if sibling.left and sibling.left.color is BLACK:
                    raise Exception("Shouldn't happen")
                if sibling.right and sibling.right.color is BLACK:
                    raise Exception("Shouldn't happen")

                if sibling is parent.left:
                    if sibling.left:
                        # i
                        if (sibling.left.color is BLACK or 
                            (sibling.right is not None and sibling.right.color is BLACK)):
                           raise Exception("Shouldn't happen: sibling has a black child in case a-i") 
                        # TODO implement
                    else:
                        # ii
                        self._left_rotate(sibling)
                        # TODO implement
                else:
                    if sibling.right:
                        # iii; there may also be a left child
                        # TODO implement
                        pass
                    else:
                        # iv 
                        if parent.color is BLACK:
                            sibling.left.color = BLACK
                        else:
                            print("second")
                            sibling.color = RED
                            sibling.left.color = BLACK
                        self._right_rotate(sibling)
                        self._left_rotate(parent)
        elif sibling.color is RED:
            # case c 
            sibling.color = BLACK
            parent.color = RED
            if sibling is parent.right:
                self._left_rotate(parent)
            else:
                self._right_rotate(parent)
            if not parent.left:
                self._hard_case_for_delete(parent.right)
            elif not parent.right:
                self._hard_case_for_delete(parent.left)
            else:
                raise Exception("Shouldn't happen: hard case c")



    def _balance(self, x):
        """ The rotations here are called either with the current x OR with its 
        grandparent 

        Left Rotation (rotate(x)): 
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
        """ (counterclockwise) x = parent; y = right child """
        y = x.right
        if x.parent:
            if x.parent.left is x: x.parent.left = y
            elif x.parent.right is x: x.parent.right = y
            else: raise Exception('Not supposed to happen')
        else:
            self.root = y

        y.parent = x.parent

        x.right = y.left
        if y.left: 
            y.left.parent = x

        x.parent = y
        y.left = x

    def _right_rotate(self, x):
        """ (clockwise) x = parent; y = left child """
        y = x.left
        if x.parent:
            if x is x.parent.right: x.parent.right = y
            elif x is x.parent.left: x.parent.left = y
            else: raise Exception('Not supposed to happen')
        else:
            self.root = y

        y.parent = x.parent

        x.left = y.right
        if y.right: 
            y.right.parent = x

        x.parent = y
        y.right = x


################################################################################
#                                 TRIE TREE                                    #
################################################################################


class AlphaTrieNode:
    def __init__(self, letter=None, parent=None):
        self.letter = letter
        if self.letter is not None:
            self.letter = self.letter.lower()
        self.parent = parent
        self.__children = None  # lazily initiate the dict for saving space
        self.is_word_contained = False

    def has_children(self):
        if len(self._get_children()) > 0:
            return True
        else:
            return False

    def has_child(self, letter):
        return letter.lower() in self._get_children()

    def add_child(self, letter):
        self._get_children()[letter.lower()] = AlphaTrieNode(letter, self)

    def get_child(self, letter):
        if not self.has_child(letter):
            return None
        return self._get_children()[letter.lower()]

    def remove_child(self, letter):
        if self.has_child(letter):
            del self._get_children()[letter.lower()]

    def _lookup_word(self):
        # Traverse up to the root to retrieve the word this node represents
        current = self
        strlist = []
        while current is not None and current.letter is not None:
            strlist.insert(0, current.letter)
            current = current.parent
        return "".join(strlist)

    def _get_children(self):
        if not self.__children:
            self.__children = dict()
        return self.__children


class AlphaTrieTree():
    """ A tree for searching words consisting of any of the 26 letters in the
    alphabet. Case insensitive, space ignored. 
    """

    def __init__(self):
        self.root = AlphaTrieNode(None)  # root node has None for its letter

    def insert(self, string):
        current_node = self.root
        for letter in string:
            if letter == ' ':
                continue
            # add letter into trie tree, if not already existing, and travel
            if not current_node.has_child(letter):
                current_node.add_child(letter)
            current_node = current_node.get_child(letter)

        # marks the word as "in" the tree
        current_node.is_word_contained = True

        self.last_inserted_node = current_node  # DEBUG PURPOSES

    def search(self, string):
        current_node = self.root
        for letter in string:
            if letter == ' ':
                continue
            if not current_node.has_child(letter):
                return False
            current_node = current_node.get_child(letter)
        return current_node.is_word_contained

    def remove(self, string):
        # search
        current = self.root
        for letter in string:
            if letter == ' ':
                continue
            if not current.has_child(letter):
                print("string to be removed not found")
                return
            current = current.get_child(letter)

        current.is_word_contained = False
        # don't actually delete any nodes if another word is in the trie tree
        # that includes this word
        if current.has_children():
            return

        while not current.is_word_contained and current is not self.root:
            # remove current from any refs
            # reassign current as parent
            current.parent.remove_child(current.letter)
            current = current.parent
