from collections import defaultdict
from pprint import pprint


class DirectedGraph:
    def __init__(self):
        self.__g = None

    def build_graph(self, pairs):
        self.__g = defaultdict(list)
        for node1, node2 in pairs:
            # add the second one to adjacency list of first
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
            for adjacent in self.__g[vertex]:
                self._dfs_recursive(adjacent, visited, result)


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
                '''add neighbors list to list. pythonian way to replace for loop and append'''
                list.extend(self.__g[data])

        return result

    def dfsWithLevelAndParent(self, s):
        '''
        BFS explores node level by level.
        Once search finishes, level will have level of each node the the BFS.
        Parent of V will have the node U which it came from during BFS
        If we trace from V to its parent and to its parent and so on till end, we reach starting node, S.
        This traced path will be one of the shortest paths from starting node S, to V
        '''
        list = []
        visited = []
        result = []
        level = {}
        parent = {s: None}
        i = 1
        if s in self.__g:
            list.append(s)
            level[s] = 0
            result.append(s)
            visited.append(s)

        while list:
            next = []
            for u in list:
                for v in self.__g[u]:
                    if v not in visited:
                        visited.append(v)
                        result.append(v)
                        level[v] = i
                        parent[v] = u
                        next.append(v)
                list = next
                i += 1

        return {'result': result, 'level': level, 'parent': parent}
