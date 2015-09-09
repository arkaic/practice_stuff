import unittest
from datastructs import graphs
from random import randrange, sample

NUM_VERTICES = 15
SAMPLESIZE = 100
MAX_INITCONNECTIONS_PER = 7

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
            num_adjacent = randrange(2, MAX_INITCONNECTIONS_PER)
            self.assertGreater(num_adjacent, 0)
            adjacents = sample(self.g.vertices, num_adjacent)
            if v in adjacents:
                adjacents.remove(v)
            v.adjacents = adjacents
            self.assertEqual(len(adjacents), len(set(adjacents)))

        for v in self.g.vertices:
            self.assertGreater(len(v.adjacents), 0)

        # connect adjacent vertices the other way around
        for v in self.g.vertices:
            for u in v.adjacents:
                for t in self.g.vertices:
                    if u is t:
                        if v not in t.adjacents:
                            t.adjacents.append(v)

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
            n = self.nums_generated

            # print('\n')
            # for v in ag.vertices:
            #     s = '[{}]: ['.format(v.element)
            #     for u in v.adjacents:
            #         s += '{}, '.format(u.element)
            #     print(s + ']')

            # get three existing vertices, two connected, one isn't 
            v = sample(ag.vertices, 1)[0]
            u = sample(v.adjacents, 1)[0]
            all_adjacents = set(v.adjacents + u.adjacents)
            while len(all_adjacents) == len(ag.vertices):
                v = sample(ag.vertices, 1)[0]
                u = sample(v.adjacents, 1)[0]
                all_adjacents = set(v.adjacents + u.adjacents)
            w = sample(ag.vertices, 1)[0]
            # print('v={} u={}'.format(v.element, u.element))
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

if __name__ == '__main__':
    unittest.main()