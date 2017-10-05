import unittest

from ds.graph import DirectedGraph, UnDirectedGraph


class TestGraph(unittest.TestCase):
    def test_build_digraph(self):
        pairs = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 8), (8, 2), (2, 9), (9, 7), (7, 6), (6, 3), (3, 5), (5, 4), (4, 6)]
        g = DirectedGraph()
        g.build_graph(pairs)
        g.print()

    def test_build_undirected_graph(self):
        pairs = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 8), (8, 2), (2, 9), (9, 7), (7, 6), (6, 3), (3, 5), (5, 4), (4, 6)]
        g = UnDirectedGraph()
        g.build_graph(pairs)
        g.print()

    def test_digraph_dfs(self):
        pairs = [(0, 1),
                 (1, 3),
                 (3, 5),
                 (5, 7),
                 (0, 2),
                 (2, 4),
                 (4, 6),
                 (6, 8)
                 ]
        g = DirectedGraph()
        g.build_graph(pairs)
        expected = g.dfs(0)
        self.assertEqual(len(expected), 9)
        self.assertEqual(expected.__str__(), [0, 2, 4, 6, 8, 1, 3, 5, 7].__str__())

    def test_digraph_bfs(self):
        pairs = [(0, 1),
                 (1, 3),
                 (3, 5),
                 (5, 7),
                 (0, 2),
                 (2, 4),
                 (4, 6),
                 (6, 8)
                 ]
        g = DirectedGraph()
        g.build_graph(pairs)
        expected = g.bfs(0)
        self.assertEqual(len(expected), 9)
        self.assertEqual(expected.__str__(), [0, 1, 2, 3, 4, 5, 6, 7, 8].__str__())

    def test_digraph_dfs_recursive(self):
        pairs = [(0, 1),
                 (1, 3),
                 (3, 5),
                 (5, 7),
                 (0, 2),
                 (2, 4),
                 (4, 6),
                 (6, 8)
                 ]
        g = DirectedGraph()
        g.build_graph(pairs)
        expected = g.dfs_recursive(0)
        self.assertEqual(len(expected), 9)
        self.assertEqual(expected.__str__(), [0, 1, 3, 5, 7, 2, 4, 6, 8].__str__())

    def test_undirectedgraph_dfsWithLevelAndParent(self):
        pairs = [(0, 1),
                 (1, 3),
                 (3, 5),
                 (5, 7),
                 (0, 2),
                 (2, 4),
                 (4, 6),
                 (6, 8)
                 ]
        g = UnDirectedGraph()
        g.build_graph(pairs)

        expected = g.dfsWithLevelAndParent(0)
        print(expected['level'])
        print(expected['parent'])

        self.assertEqual(len(expected['result']), 9)
        self.assertEqual(expected['result'].__str__(), [0, 1, 2, 3, 4, 5, 6, 7, 8].__str__())


if __name__ == '__main__':
    unittest.main()
