def _parent_index(child_index):
    return (child_index - 1) // 2  # / is float division and // is integer division


def _right_child_index(parent_index):
    return (2 * parent_index) + 2


def _left_child_index(parent_index):
    return (2 * parent_index) + 1


def _has_parent(child_index):
    return _parent_index(child_index) >= 0


def _has_right_child(parent_index, size):
    return _right_child_index(parent_index) <= size


def _has_left_child(parent_index, size):
    return _left_child_index(parent_index) <= size


class MinHeap:
    def __init__(self):
        self.__arr = []
        self.__size = 0

    def insert(self, data):
        self.__arr.append(data)
        self.__size += 1
        self.__heapify_up()

    def __heapify_up(self):
        index = self.__size - 1
        while _has_parent(index) and self.__arr[index] < self.__parent(index):
            self.__swap(index, _parent_index(index))
            index = _parent_index(index)

    def __parent(self, child_index):
        return self.__arr[_parent_index(child_index)]

    def __right_child(self, parent_index):
        return self.__arr[_right_child_index(parent_index)]

    def __left_child(self, parent_index):
        return self.__arr[_left_child_index(parent_index)]

    def __swap(self, index1, index2):
        temp = self.__arr[index1]
        self.__arr[index1] = self.__arr[index2]
        self.__arr[index2] = temp

    def remove(self):
        data = self.__arr[0]
        self.__arr[0] = self.__arr[self.__size - 1]
        self.__size -= 1
        self.__heapify_down()
        return data

    def __heapify_down(self):
        index = 0
        while _has_left_child(index, self.__size):
            min_index = _left_child_index(index)
            if _has_right_child(index, self.__size) and self.__arr[_right_child_index(index)] < self.__arr[min_index]:
                min_index = _right_child_index(index)

            if self.__arr[index] > self.__arr[min_index]:
                self.__swap(index, min_index)
            else:
                break
            index = min_index

    def min(self):
        return self.__arr[0]


class MaxHeap:
    def __init__(self):
        self.__arr = []
        self.__size = 0

    def insert(self, data):
        self.__arr.append(data)
        self.__size += 1
        self.__heapify_up()

    def __heapify_up(self):
        index = self.__size - 1
        while _has_parent(index) and self.__arr[index] > self.__parent(index):
            self.__swap(index, _parent_index(index))
            index = _parent_index(index)

    def __parent(self, child_index):
        return self.__arr[_parent_index(child_index)]

    def __right_child(self, parent_index):
        return self.__arr[_right_child_index(parent_index)]

    def __left_child(self, parent_index):
        return self.__arr[_left_child_index(parent_index)]

    def __swap(self, index1, index2):
        temp = self.__arr[index1]
        self.__arr[index1] = self.__arr[index2]
        self.__arr[index2] = temp

    def remove(self):
        data = self.__arr[0]
        self.__arr[0] = self.__arr[self.__size - 1]
        self.__size -= 1
        self.__heapify_down()
        return data

    def __heapify_down(self):
        index = 0
        while _has_left_child(index, self.__size):
            min_index = _left_child_index(index)
            if _has_right_child(index, self.__size) and self.__arr[_right_child_index(index)] > self.__arr[min_index]:
                min_index = _right_child_index(index)

            if self.__arr[index] < self.__arr[min_index]:
                self.__swap(index, min_index)
            else:
                break
            index = min_index

    def max(self):
        return self.__arr[0]
