class SListNode:
    def __init__(self, data=None, next_node=None):
        self.__data = data
        self.__next = next_node

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class SLinkedList:
    def __init__(self, head=None, tail=None):
        self.__head = head
        self.__tail = tail

    def insert(self, data):
        new_node = SListNode(data)
        if not self.__head:
            self.__tail = self.__head = new_node
            return

        self.__tail.set_next(new_node)
        self.__tail = new_node

    def insert_from_list(self, data):
        for d in data:
            self.insert(d)

    def print_list(self):
        print("Printing")
        node = self.__head
        while node:
            print(node.data)
            node = node.next

    def print_list_reverse(self):
        self.__print_list_reverse(self.__head)

    def __print_list_reverse(self, node=None):
        if not node:
            return
        self.__print_list_reverse(node.get_next())
        print(node.get_data())
