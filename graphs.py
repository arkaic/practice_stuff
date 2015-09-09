
class Vertex:
    def __init__(self, edge):
        self.vertices = []

# class Edge:
#     def __init__(self, v, u):
#         self.v = v
#         self.u = u

class AdjListGraph:

    def __init__(self, path=None):
        self.adj_list = []

        if path:
            # load adjlist specs from file 
            # add to adj_list and edges
            pass

    def insert_edge(self, v, u):
        if not is_edge(v, u):
            self.adj_list.append([v, u])
            self.adj_list.append([u, v])

    def is_edge(self, v, u):
        for adjacents in self.adj_list:
            if adjacents[0] == v:
                if u not in adjacents:
                    return False
            elif adjacents[0] == u:
                if v not in adjacents:
                    return False
        return True

    def remove_edge(self):
        pass

    def insert_vertex(self, v):
        for a in self.adj_list:
            if a[0] == v:
                return False
        self.adj_list.append([v])
        return True
