import unittest
from ds.heap import MinHeap, MaxHeap
import sys, os
sys.path.insert(0, os.path.abspath('..'))

class HeapTest(unittest.TestCase):
    def test_minheap(self):
        minheap = MinHeap()
        for i in [2, 5, 7, 4, 9, 21, 0, 87, 1]:
            minheap.insert(i)

        self.assertEqual(minheap.min(), 0)
        minheap.remove()
        self.assertEqual(minheap.min(), 1)

    def test_maxheap(self):
        maxheap = MaxHeap()
        for i in [2, 5, 7, 4, 9, 21, 0, 87, 1]:
            maxheap.insert(i)

        self.assertEqual(maxheap.max(), 87)
        maxheap.remove()
        self.assertEqual(maxheap.max(), 21)





if __name__ == '__main__':
    unittest.main()
