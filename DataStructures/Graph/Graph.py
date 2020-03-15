from DataStructures.LinkedList.LinkedList import LinkedList


class Graph:
    def __init__(self, vertices, is_directed=True):
        self.is_directed = is_directed
        # Total number of vertices in the Graph
        self.vertices = vertices
        # Dictionary that holds the adjacency list for all the vertices
        self.adjacency_list = {}

    def _add_edge_helper(self, source, destination):
        if source in self.adjacency_list:
            adjacency_list_of_source = self.adjacency_list[source]
        else:
            adjacency_list_of_source = LinkedList()
        adjacency_list_of_source.insert(destination, 0)
        self.adjacency_list[source] = adjacency_list_of_source

    def add_edge(self, source, destination):
        if self.is_directed is False:
            self._add_edge_helper(destination, source)

        self._add_edge_helper(source, destination)

    def add_edges(self, list_of_edges):
        for edge in list_of_edges:
            self.add_edge(edge[0], edge[1])

    def print_graph(self):
        for key in self.adjacency_list:
            adjacency_list_of_key = self.adjacency_list[key]
            print('{0} => '.format(key), end='')
            adjacency_list_of_key.print_list()


