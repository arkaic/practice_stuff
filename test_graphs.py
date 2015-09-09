import unittest
from datastructs import graphs
from random import randrange, sample

NUM_VERTICES = 15
SAMPLESIZE = 10

class TestAdjListGraph(unittest.TestCase):

    def setUp(self):
        self.g = graphs.AdjListGraph()
        self.nums_generated = []

        # generate vertices into a temp list, l
        c = 0
        while c < NUM_VERTICES:
            n = randrange(100)
            while n in self.nums_generated:
                n = randrange(100)
            self.nums_generated.append(n)
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
            num_adjacent = randrange(1, NUM_VERTICES - 1)
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
                            self.assertEqual(len(t.adjacents), len(set(t.adjacents)))    
            self.assertEqual(len(v.adjacents), len(set(v.adjacents)))

        for v in self.g.vertices:
            self.assertEqual(len(v.adjacents), len(set(v.adjacents)))
            self.assertLessEqual(len(v.adjacents), NUM_VERTICES)

    def tearDown(self):
        self.g = None
        self.nums_generated = []

    def test_isedge(self):
        for i in range(SAMPLESIZE):
            if not self.g:
                self.setUp()

            graph = self.g

            a = randrange(100)
            b = randrange(100)
            while a in self.nums_generated or b in self.nums_generated:
                a = randrange(100)
                b = randrange(100)

            s = graphs.Vertex(a)
            t = graphs.Vertex(b)

            for v in graph.vertices:
                # u is randomly chosen from adjacent vertices of vertex
                u = sample(v.adjacents, 1)[0]
                self.assertTrue(graph.is_edge(v, u))
                self.assertTrue(graph.is_edge(u, v))
                self.assertFalse(graph.is_edge(v, s))
                self.assertFalse(graph.is_edge(a, v))
                self.assertFalse(graph.is_edge(s, t))
                self.assertFalse(graph.is_edge(t, s))

            self.tearDown()

if __name__ == '__main__':
    unittest.main()