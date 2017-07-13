import unittest
import sys, os

from ds.stack import Stack


class StackTest(unittest.TestCase):
    def test_stack(self):
        stack = Stack()
        for i in [23, 4, 2, 56]:
            stack.push(i)

        self.assertEqual(stack.size(), 4)
        self.assertEqual(stack.peek(), 56)
        self.assertEqual(stack.pop(), 56)
        stack.pop()
        stack.pop()
        stack.pop()
        self.assertEqual(stack.size(), 0)
        self.assertRaises(RuntimeError, stack.pop)

    def test_stack_with_list(self):
        stack = Stack()
        for i in [23, 4, 2, 56]:
            stack.push(i)

        self.assertEqual(stack.size(), 4)
        self.assertEqual(stack.peek(), 56)
        self.assertEqual(stack.pop(), 56)
        stack.pop()
        stack.pop()
        stack.pop()
        self.assertEqual(stack.size(), 0)
        self.assertRaises(RuntimeError, stack.pop)


if __name__ == '__main__':
    unittest.main()
