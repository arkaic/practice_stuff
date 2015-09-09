class Vertex:
    def __init__(self, edge):
        self.vertices = []

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
            return True
        return False

    def is_edge(self, v, u):
        for adjacents in self.adj_list:
            if adjacents[0] == v or adjacents[0] == u:
                if u in adjacents[1:] or v in adjacents[1:]:
                    return True
                else:
                    return False
        return False

    def remove_edge(self):
        pass
