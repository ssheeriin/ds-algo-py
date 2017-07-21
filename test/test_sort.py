import unittest
from search_sort.sort import quick_sort, merge_sort


class TestSort(unittest.TestCase):
    def test_quick_sort(self):
        array = [2, 5, 8, 4, 1, 3, 9, 15, 6, 7]
        quick_sort(array)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
        self.assertEqual(expected, array)

        array = [2, 5, 8, 4, 5]
        quick_sort(array)
        expected = [2, 4, 5, 5, 8]
        self.assertEqual(expected, array)

        array = []
        quick_sort(array)
        expected = []
        self.assertEqual(expected, array)

        array = [2, 5, -8, 4, -5]
        quick_sort(array)
        expected = [-8, -5, 2, 4, 5]
        self.assertEqual(expected, array)

    def test_merge_sort(self):
        array = [2, 5, 8, 4, 1, 3, 9, 15, 6, 7]
        merge_sort(array)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
        self.assertEqual(expected, array)

        array = [2, 5, 8, 4, 5]
        merge_sort(array)
        expected = [2, 4, 5, 5, 8]
        self.assertEqual(expected, array)

        array = []
        merge_sort(array)
        expected = []
        self.assertEqual(expected, array)

        array = [2, 5, -8, 4, -5]
        merge_sort(array)
        expected = [-8, -5, 2, 4, 5]
        self.assertEqual(expected, array)


if __name__ == '__main__':
    unittest.main()
