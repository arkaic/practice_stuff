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
            if self.l[i].element == el:
                return True
            elif el < self.l[i].element:
                i *= 2
            elif el > self.l[i].element:
                i = i * 2 + 1

        print("i={}".format(i))
        return False

    def insert(self, el):
        self.count += 1

    def delete(self, el):
        if self.count > 0:
            self.count -= 1
