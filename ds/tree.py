class TreeNode:
    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None
        self.__parent = None

    def data(self):
        return self.__data

    def left(self):
        return self.__left

    def right(self):
        return self.__right

    def set_data(self, data):
        self.__data = data

    def set_left(self, left):
        self.__left = left

    def parent(self):
        return self.__parent

    def set_parent(self, parent):
        self.__parent = parent

    def set_right(self, right):
        self.__right = right

    def __str__(self) -> str:
        return self.__data


class BST:
    def __init__(self):
        self.__prev = None
        self.__root = None

    def add(self, data):
        self.__root = self._add(self.__root, data)

    def add_all(self, data_list):
        for data in data_list:
            self.__root = self._add(self.__root, data)

    def _add(self, node, data):
        if not node:
            return TreeNode(data)

        if data <= node.data():
            left_temp = self._add(node.left(), data)
            node.set_left(left_temp)
            left_temp.set_parent(node)
        else:
            temp_right = self._add(node.right(), data)
            node.set_right(temp_right)
            temp_right.set_parent(node)

        return node

    def in_order(self):
        result = []
        self._in_order(self.__root, result)
        return result

    def _in_order(self, node, result):
        if not node:
            return

        self._in_order(node.left(), result)
        result.append(node.data())
        self._in_order(node.right(), result)

    def pre_order(self):
        result = []
        self._pre_order(self.__root, result)
        return result

    def _pre_order(self, node, result):
        if not node:
            return

        result.append(node.data())
        self._pre_order(node.left(), result)
        self._pre_order(node.right(), result)

    def post_order(self):
        result = []
        self._post_order(self.__root, result)
        return result

    def _post_order(self, node, result):
        if not node:
            return

        self._post_order(node.left(), result)
        self._post_order(node.right(), result)
        result.append(node.data())

    def is_bst(self):
        return self._is_bst(self.__root)

    def parent(self, data):
        node = self._find(self.__root, data)
        if node and node.parent():
            return node.parent().data()
        else:
            return None

    def _is_bst(self, node):
        if not node:
            return True

        if not self._is_bst(node.left()):
            return False

        if self.__prev is not None and self.__prev.data() > node.data():
            return False

        self.__prev = node

        return self._is_bst(node.right())

    def _find(self, node, data):
        if not node:
            return None

        result = self._find(node.left(), data)
        if result:
            return result

        if node.data() == data:
            return node

        return self._find(node.right(), data)

    def successor_in_order(self, data, method):
        self.__prev = None

        methods = {
            "with-prev-pointer": self._successor_in_order_with_prev_pointer,
            "with-parent-pointer": self._successor_in_order_with_parent_pointer
        }

        successor = methods[method](self.__root, data)

        if successor:
            return successor.data()
        else:
            return None

    def _successor_in_order_with_parent_pointer(self, root, data):
        '''find successor with parent pointer'''
        '''this is bases on the following 2 properties'''
        ''' 
        1) if node's right subtree is NOT NULL, successor lies in right subtree and 
            is the lowest node in the right subtree 
        2) if node's right subtree is  NULL, successor is one of the ancestors
        2.1) travel up the parents till we see a node which is the left child of its parent. parent of that node is
            the successor
        '''

        node = self._find(root, data)

        if not node:
            raise RuntimeError("data not found in tree")

        successor_node = None
        if node.right():
            successor_node = self.min_node(node.right())
        else:

            child = node
            p = child.parent()
            while p:
                if p.right() != child:
                    break
                child = p
                p = child.parent()

            successor_node = p

        return successor_node

    def _successor_in_order_with_prev_pointer(self, node, data):
        if not node:
            return None

        left = self._successor_in_order_with_prev_pointer(node.left(), data)
        if left:
            return left

        if self.__prev and self.__prev.data() == data:
            return node
        else:
            self.__prev = node

        return self._successor_in_order_with_prev_pointer(node.right(), data)

    def remove(self, data):
        data_node = self._find(self.__root, data)  # node to be removed
        temp = data_node.data()

        if not data_node:
            raise RuntimeError("data not found in tree")

        if None in (data_node.left() and data_node.right()):
            ''' node has no children'''
            ''' then just remove node '''

            return data_node.data()

        if data_node.left() and data_node.right():
            ''' node has 2 children '''
            ''' then copy ine in order successor to here and delete the successor'''
        else:
            ''' node has one child'''
            ''' then copy the child to here and remove child'''

        return temp

    def min_node(self, node):
        prev = None
        while node:
            prev = node
            node = node.left()

        return prev
