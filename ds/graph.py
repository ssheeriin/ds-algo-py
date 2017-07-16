from collections import defaultdict
from pprint import pprint


class DirectedGraph:
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

    def dfs_recursive(self, start):
        visited = []
        result = []
        self._dfs_recursive(start, visited, result)
        return result

    def _dfs_recursive(self, vertex, visited, result):
        if vertex not in visited:
            result.append(vertex)
            visited.append(vertex)
            for adj in self.__g[vertex]:
                self._dfs_recursive(adj, visited, result)


class UnDirectedGraph:
    def __init__(self):
        self.__g = None

    def build_graph(self, pairs):
        self.__g = defaultdict(list)
        for node1, node2 in pairs:
            self.__g[node1].append(node2)
            self.__g[node2].append(node1)

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
