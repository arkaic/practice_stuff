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
        if root: self.count += 1
    
    def search(self, el):
        def _dfs(node):
            if not node or el == node.element: return node
            elif el < node.element: return _dfs(node.left)
            else: return _dfs(node.right)
        return _dfs(self.root)

    def insert(self, el):
        def _dfi(node):
            if el == node.element:
                return False  # already exists
            elif el < node.element:
                if node.left: 
                    return _dfi(node.left)
                else: 
                    node.left = Node(el, parent=node)
            else:
                if node.right: 
                    return _dfi(node.right)
                else: 
                    node.right = Node(el, parent=node)
            self.count += 1
            return True

        if not self.root:
            self.root = Node(el)
            return True
        return _dfi(self.root)

    def delete(self, el):
        node = self.search(el)

        if not node:
            return False

        if not node.right:
            node.left.parent = node.parent
            node.parent.left = node.left
        elif not node.left:
            node.right.parent = node.parent
            node.parent.right = node.right
        else:
            # Get smallest node in right subtree
            subtree_node = node.right
            while subtree_node.left: subtree_node = subtree_node.left

            # connect subtree node's right child to subtree node's parent
            # substitute subtree node in place of the node to be deleted
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

