import unittest

from ds.tree import BST


class TestTree(unittest.TestCase):
    def test_in_order(self):
        tree = BST()
        tree.add_all([8, 3, 1, 6, 7, 4, 10, 14, 13])
        expected = tree.in_order()
        self.assertEqual(expected.__str__(), [1, 3, 4, 6, 7, 8, 10, 13, 14].__str__())

    def test_pre_order(self):
        tree = BST()
        tree.add_all([8, 3, 1, 6, 7, 4, 10, 14, 13])
        expected = tree.pre_order()
        self.assertEqual(expected.__str__(), [8, 3, 1, 6, 4, 7, 10, 14, 13].__str__())

    def test_post_order(self):
        tree = BST()
        tree.add_all([8, 3, 1, 6, 7, 4, 10, 14, 13])
        expected = tree.post_order()
        self.assertEqual(expected.__str__(), [1, 4, 7, 6, 3, 13, 14, 10, 8].__str__())

    def test_is_bst(self):
        tree = BST()
        tree.add_all([8, 3, 1, 6, 7, 4, 10, 14, 13])
        self.assertTrue(tree.is_bst())

    def test_parent(self):
        tree = BST()
        tree.add_all([8, 3, 1, 6, 7, 4, 10, 14, 13])
        self.assertEqual(tree.parent(1), 3)
        self.assertEqual(tree.parent(3), 8)
        self.assertEqual(tree.parent(8), None)
        self.assertEqual(tree.parent(14), 10)
        self.assertEqual(tree.parent(13), 14)

    def test_successor_in_order(self):
        tree = BST()
        tree.add_all([20, 8, 4, 12, 14, 10, 22])
        self.assertEqual(tree.successor_in_order(8, "with-prev-pointer"), 10)
        self.assertEqual(tree.successor_in_order(10, "with-prev-pointer"), 12)
        self.assertEqual(tree.successor_in_order(14, "with-prev-pointer"), 20)
        self.assertEqual(tree.successor_in_order(22, "with-prev-pointer"), None)

        self.assertEqual(tree.successor_in_order(8, "with-parent-pointer"), 10)
        self.assertEqual(tree.successor_in_order(10, "with-parent-pointer"), 12)
        self.assertEqual(tree.successor_in_order(14, "with-parent-pointer"), 20)
        self.assertEqual(tree.successor_in_order(22, "with-parent-pointer"), None)


        # def test_remove(self):
        #     tree = BST()
        #     tree.add_all([8, 3, 1, 6, 7, 4, 10, 14, 13])
        #     tree.remove(13)
        #     self.assertEqual(tree.pre_order().__str__(), [8, 3, 1, 6, 4, 7, 10, 14].__str__())


if __name__ == '__main__':
    unittest.main()
