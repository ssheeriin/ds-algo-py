class StackNode:
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    def get_next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data


class Stack:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def push(self, data):
        newNode = StackNode(data)
        if not self.__head:
            self.__head = newNode
        else:
            newNode.set_next(self.__head)
            self.__head = newNode
        self.__size += 1

    def peek(self):
        return self.__head.get_data()

    def size(self):
        return self.__size

    def pop(self):
        if self.size() == 0:
            raise RuntimeError("stack empty")

        data = self.__head.get_data()
        self.__head = self.__head.get_next()
        self.__size -= 1
        return data


class StackWithList:
    def __init__(self):
        self.__items = []

    def push(self, data):
        self.__items.append(data)

    def peek(self):
        if self.size() == 0:
            raise RuntimeError("Stack is Empty")

        return self.__items[self.size() - 1]

    def pop(self):
        if self.size() == 0:
            raise RuntimeError("Stack is Empty")

        return self.__items.pop()

    def size(self):
        return len(self.__items)
