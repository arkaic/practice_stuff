class Node:
    def __init__(self, element, index):
        self.element = element
        self.index = index


class BinarySearchTree:

    def __init__(self, l=None):        
        self.l = l  # or I can make a Node with element=None
        if not self.l:
            self.l = [None]
        self.count = 0
    
    def search(self, el):
        if len(self.l) < 2: return False
        i = 1
        while i < len(self.l) and self.l[i] is not None:
            if el < self.l[i].element: i *= 2
            elif el > self.l[i].element: i = i * 2 + 1
            else: return True
        return False

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
        if self.count > 0:
            self.count -= 1
