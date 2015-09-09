
class Vertex:
    def __init__(self, element=None, adjacents=[]):
        self.element = element
        self.adjacents = adjacents


class AdjListGraph:
    def __init__(self, path=None, vertices=None):
        self.vertices = vertices
        if vertices is None:
            self.vertices = []
        if path:
            # load adjlist specs from file 
            # add to vertices and edges
            pass

    def insert_edge(self, v, u):
        if not self.is_edge(v, u):
            if v not in self.vertices: self.vertices.append(v)
            if u not in self.vertices: self.vertices.append(u)
            v.adjacents.append(u)
            u.adjacents.append(v)
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

    def remove_edge(self, v, u):
        if self.is_edge(v, u):
            try:
                v.adjacents.remove(u)
                u.adjacents.remove(v)
            except ValueError:
                raise Exception("Shouldn't happen when removing existing edge")
            return True
        return False
