
class Vertex:
    def __init__(self, element=None):
        self.adjacents = []
        self.element = element


class AdjListGraph:
    def __init__(self, path=None):
        self.vertices = []
        if path:
            # load adjlist specs from file 
            # add to vertices and edges
            pass

    def insert_edge(self, v, u):
        if not is_edge(v, u):
            v.adjacents.append(u)
            u.adjacents.append(v)
            if v not in self.vertices: self.vertices.append(v)
            if u not in self.vertices: self.vertices.append(u)
            return True
        return False

    def is_edge(self, v, u):
        for vertex in self.vertices:
            if vertex is v or vertex is u:
                if u in vertex.adjacents or v in vertex.adjacents:
                    return True
                else:
                    return False
        return False

    def remove_edge(self):
        pass
