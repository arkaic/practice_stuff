import unittest
from datastructs import graphs
from random import randrange, sample

NUM_VERTICES = 15
SAMPLESIZE = 100
MAX_INITCONNECTIONS_PER = 7

class TestAdjListGraph(unittest.TestCase):

    def setUp(self):
        self.g = graphs.AdjListGraph()
        self.generated_nums = []

        # generate vertices into a temp list, l
        c = 0
        while c < NUM_VERTICES:
            n = randrange(100)
            while n in self.generated_nums:
                n = randrange(100)
            self.generated_nums.append(n)
            v = graphs.Vertex(n)
            if v not in self.g.vertices:
                self.g.vertices.append(v)
                c += 1

        # Assert there are NUM_VERTICES unique vertices in the graph
        self.assertEqual(NUM_VERTICES, len(self.g.vertices))
        self.assertEqual(NUM_VERTICES, len(set(self.g.vertices)))

        # generate adjacent vertices for each generated vertex
        for v in self.g.vertices:
            # randomize amount of adjacents
            num_adjacent = randrange(2, MAX_INITCONNECTIONS_PER)
            adjacents = sample(self.g.vertices, num_adjacent)
            if v in adjacents:
                adjacents.remove(v)
            v.adjacents = adjacents
            self.assertEqual(len(adjacents), len(set(adjacents)))

        # connect adjacent vertices the other way around
        for v in self.g.vertices:
            for u in v.adjacents:
                for t in self.g.vertices:
                    if u is t:
                        if v not in t.adjacents:
                            t.adjacents.append(v)

        # assert that every vertex is connected to at least 1 other
        for v in self.g.vertices:
            self.assertGreater(len(v.adjacents), 0)

        # make sure every adjacency list is unique, does not contain vertices
        # that do not exist, and are connected both ways
        for v in self.g.vertices:
            self.assertTrue(v not in v.adjacents)
            self.assertGreater(len(v.adjacents), 0)
            self.assertEqual(len(v.adjacents), len(set(v.adjacents)))
            self.assertLessEqual(len(v.adjacents), NUM_VERTICES)
            for u in v.adjacents:
                for t in self.g.vertices:
                    if t is u:
                        self.assertTrue(v in t.adjacents)

    def tearDown(self):
        self.g = None
        self.generated_nums = []

    def test_isedge(self):
        for i in range(SAMPLESIZE):
            if not self.g:
                self.setUp()

            graph = self.g

            a = randrange(100)
            b = randrange(100)
            while a in self.generated_nums or b in self.generated_nums:
                a = randrange(100)
                b = randrange(100)

            s = graphs.Vertex(a)
            t = graphs.Vertex(b)

            for v in graph.vertices:
                # u is randomly chosen from adjacent vertices of vertex
                len('pop={}'.format(v.adjacents))
                u = sample(v.adjacents, 1)[0]
                self.assertTrue(graph.is_edge(v, u))
                self.assertTrue(graph.is_edge(u, v))
                self.assertFalse(graph.is_edge(v, s))
                self.assertFalse(graph.is_edge(a, v))
                self.assertFalse(graph.is_edge(s, t))
                self.assertFalse(graph.is_edge(t, s))

            self.tearDown()

    def test_insert_edge(self):
        for i in range(SAMPLESIZE):
            if not self.g:
                self.setUp()

            ag = self.g
            n = self.generated_nums

            # get two existing connected vertices
            v = sample(ag.vertices, 1)[0]
            u = sample(v.adjacents, 1)[0]
            all_adjacents = set(v.adjacents + u.adjacents)
            while len(all_adjacents) == len(ag.vertices):
                v = sample(ag.vertices, 1)[0]
                u = sample(v.adjacents, 1)[0]
                all_adjacents = set(v.adjacents + u.adjacents)

            # get existing vertex not connected to v or u
            w = sample(ag.vertices, 1)[0]
            while w in all_adjacents:
                w = sample(ag.vertices, 1)[0]
            self.assertTrue(ag.is_edge(v, u))
            self.assertFalse(ag.is_edge(v, w))
            self.assertFalse(ag.is_edge(u, w))

            # make new vertices s and t
            i, j, k = randrange(100), randrange(100), randrange(100)
            while i in n or j in n or k in n:
                i, j, k = randrange(100), randrange(100), randrange(100)
            s, t, r = graphs.Vertex(i), graphs.Vertex(j), graphs.Vertex(k)

            # v,u,w exist in graph, but w not connected to other two
            # s,t do not exist in graph
            self.assertFalse(ag.insert_edge(v, u))
            self.assertFalse(ag.insert_edge(u, v))
            self.assertTrue(ag.insert_edge(v, w))
            self.assertTrue(ag.insert_edge(u, w))
            self.assertTrue(ag.insert_edge(u, s))
            self.assertTrue(ag.insert_edge(t, r))
            self.assertFalse(ag.insert_edge(v, w))
            self.assertFalse(ag.insert_edge(u, w))
            self.assertFalse(ag.insert_edge(u, s))
            self.assertFalse(ag.insert_edge(t, r))

            self.tearDown()

    def test_remove_edge(self):
        for i in range(SAMPLESIZE):
            if not self.g:
                self.setUp()

            ag = self.g
            n = self.generated_nums

            # existing vertices
            v = sample(ag.vertices, 1)[0]
            u = sample(v.adjacents, 1)[0]
            all_adjacents = set(v.adjacents + u.adjacents)
            while len(all_adjacents) == len(ag.vertices):
                v = sample(ag.vertices, 1)[0]
                u = sample(v.adjacents, 1)[0]
                all_adjacents = set(v.adjacents + u.adjacents)

            # get existing vertex not connected to v or u
            w = sample(ag.vertices, 1)[0]
            while w in all_adjacents:
                w = sample(ag.vertices, 1)[0]
            self.assertTrue(ag.is_edge(v, u))
            self.assertFalse(ag.is_edge(v, w))
            self.assertFalse(ag.is_edge(u, w))

            # make new vertices s and t
            i, j, k = randrange(100), randrange(100), randrange(100)
            while i in n or j in n or k in n:
                i, j, k = randrange(100), randrange(100), randrange(100)
            s, t, r = graphs.Vertex(i), graphs.Vertex(j), graphs.Vertex(k)

            # v,u,w exists
            # s,t,r dont

            self.assertFalse(ag.remove_edge(v, w))
            self.assertFalse(ag.remove_edge(v, s))
            self.assertFalse(ag.remove_edge(w, s))
            self.assertFalse(ag.remove_edge(s, t))
            self.assertTrue(ag.remove_edge(v, u))
            self.assertFalse(ag.remove_edge(v, u))
            self.assertFalse(ag.remove_edge(u, v))

            self.tearDown()

    def test_dfs(self):
        for i in range(SAMPLESIZE):
            if not self.g:
                self.setUp()
            ag = self.g
            n = self.generated_nums

            graphs.traverse(ag, graphs.DFS)
            for v in ag.vertices:
                self.assertTrue(v.visited)

            self.tearDown()

    def test_bfs(self):
        for i in range(SAMPLESIZE):
            if not self.g:
                self.setUp()

            graphs.traverse(self.g, graphs.BFS)
            for v in self.g.vertices:
                self.assertTrue(v.visited)

            self.tearDown()


if __name__ == '__main__':
    unittest.main()