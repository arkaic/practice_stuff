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
        if not self.search(el):
            self.count += 1
            i = 1

            # Re-search again to find spot (can avoid this if 
            # search() returns an index)
            while i < len(self.l) and self.l[i] is not None:
                if el < self.l[i].element: i *= 2
                else: i = i * 2 + 1

            # Resize list if insertion point is on new level
            if i >= len(self.l):
                new_l = [None] * len(self.l) * 2
                for index, node in enumerate(self.l):
                    if node: new_l[index] = node
                self.l = new_l

            self.l[i] = Node(el, i)
            return True
        else: return False

    def delete(self, el):
        if self.count > 0 and self.search(el):
            self.count -= 1
            i = 1
            while i < len(self.l) and self.l[i] is not None:
                if el < self.l[i].element: i *= 2
                elif el > self.l[i].element: i = i * 2 + 1
                else: break

            if i >= len(self.l) or self.l[i] is None: return False

            deleted_node = self.l[i]
            self.l[i] = None

            j = i * 2 + 1
            while True:
                if j*2 >= len(self.l) or self.l[j*2] is None:
                    break
                j *= 2

            if j == i * 2 + 1:
                pass # TODO 

            # delete node, get smallest child of right subtree and sub in
            # if smallest child has right children, connect that with its old parent

