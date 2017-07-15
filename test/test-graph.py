import unittest

from ds.graph import graph


class TestGraph(unittest.TestCase):
    def test_build_graph(self):
        pairs = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 8), (8, 2), (2, 9), (9, 7), (7, 6), (6, 3), (3, 5), (5, 4), (4, 6)]
        g = graph()
        g.build_graph(pairs)
        g.print()

    def test_dfs(self):
        pairs = [(0, 1),
                 (1, 2),
                 (2, 3),
                 (3, 4),
                 (0, 8),
                 (8, 2),
                 (2, 9),
                 (9, 7),
                 (7, 6),
                 (6, 3),
                 (3, 5),
                 (5, 4),
                 (4, 6)]
        g = graph()
        g.build_graph(pairs)
        expected = g.dfs(0)
        self.assertEqual(len(expected), 10)
        self.assertEqual(expected.__str__(), [0, 8, 2, 9, 7, 6, 3, 5, 4, 1].__str__())

    def test_bfs(self):
        pairs = [(0, 1),
                 (1, 2),
                 (2, 3),
                 (3, 4),
                 (0, 8),
                 (8, 2),
                 (2, 9),
                 (9, 7),
                 (7, 6),
                 (6, 3),
                 (3, 5),
                 (5, 4),
                 (4, 6)]
        g = graph()
        g.build_graph(pairs)
        expected = g.bfs(0)
        self.assertEqual(len(expected), 10)
        self.assertEqual(expected.__str__(), [0, 1, 8, 2, 3, 9, 4, 5, 7, 6].__str__())


if __name__ == '__main__':
    unittest.main()
