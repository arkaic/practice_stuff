import unittest, graphs, random

NUM_VERTICES = 15

class TestAdjListGraph(unittest.TestCase):
    def setUp(self):
        self.g = graphs.AdjListGraph()

        # generate vertices into a temp list, l
        self.l = []
        c = 0
        while c < NUM_VERTICES:
            v = random.randrange(100)
            if v not in self.l:
                self.l.append(v)
                c += 1
        self.assertEqual(len(self.l), NUM_VERTICES)
        print("vertices generated: {}".format(self.l))

        # generate adjacent vertices for each generated vertex
        for v in self.l:
            # randomize how much adjacents
            num_adjacent = random.randrange(len(self.l) - 1)  
            adjacents = random.sample(self.l, num_adjacent)
            if v in adjacents:
                adjacents.remove(v)
            adjacents = [v] + adjacents  # prefix v to the list
            self.g.adj_list.append(adjacents)
            print(adjacents)

        print("\n\n\n\n")

        # connect adjacent vertices the other way around
        for adjacents in self.g.adj_list:
            for u in adjacents:
                if u != adjacents[0]:
                    for adjs in self.g.adj_list:
                        if adjs[0] == u:
                            if not adjacents[0] in adjs:
                                adjs.append(adjacents[0])

        print("FINAL")
        for adj in self.g.adj_list:
            self.assertEqual(len(adj), len(set(adj)))
            self.assertLessEqual(len(adj), NUM_VERTICES)
            print(adj)

    def test_isedge(self):
        graph = self.g
        a = random.randrange(100)
        while a in self.l:
            a = random.randrange(100)
        for adjacents in graph.adj_list:
            u = random.sample(adjacents[1:], 1)[0]            
            self.assertTrue(graph.is_edge(adjacents[0], u))
            self.assertTrue(graph.is_edge(u, adjacents[0]))
            self.assertFalse(graph.is_edge(adjacents[0], a))
            self.assertFalse(graph.is_edge(a, adjacents[0]))



if __name__ == '__main__':
    unittest.main()