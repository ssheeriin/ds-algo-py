from collections import defaultdict
from pprint import pprint


class gnode:
    def __init__(self, data):
        self.__data = data
        self.__visited = False

    def __eq__(self, other):
        return self.__data == other.data()

    def data(self):
        return self.__data

    def set_visited(self, visited=False):
        self.__visited = visited

    def visited(self):
        return self.__visited

    def __hash__(self):
        return hash(self.__data)

    def __str__(self):
        return self.__data


class graph:
    def __init__(self):
        self.__g = None

    def build_graph(self, pairs):
        self.__g = defaultdict(list)
        for node1, node2 in pairs:
            self.__g[node1].append(node2)

    def dfs(self, start_node):
        stack = []
        visited = []
        result = []
        if start_node in self.__g:
            stack.append(start_node)

        while stack:
            data = stack.pop()
            if data not in visited:
                result.append(data)
                visited.append(data)
                for adj in self.__g[data]:
                    stack.append(adj)
        return result

    def print(self):
        pprint(self.__g)

    def bfs(self, start_node):
        list = []
        visited = []
        result = []
        if start_node in self.__g:
            list.append(start_node)

        while list:
            data = list.pop(0)
            if data not in visited:
                result.append(data)
                visited.append(data)
                for adj in self.__g[data]:
                    list.append(adj)
        return result
