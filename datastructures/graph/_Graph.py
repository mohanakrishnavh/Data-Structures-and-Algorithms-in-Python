class Vertex:
    def __init__(self, val):
        self.value = val
        self.connectedTo = {}

    def add_neighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def get_connections(self):
        return self.connectedTo.keys()

    def get_value(self):
        return self.value

    def get_weight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.value)+" connected to: "+str([x.value for x in self.connectedTo])


class Graph:
    def __init__(self):
        self.vertex_list = {}
        self.vertex_count = 0

    def add_vertex(self, value):
        self.vertex_count += 1
        vertex = Vertex(value)
        self.vertex_list[value] = vertex
        return vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        if from_vertex not in self.vertex_list:
            vertex = self.add_vertex(from_vertex)
        if to_vertex not in self.vertex_list:
            vertex = self.add_vertex(to_vertex)

        self.vertex_list[from_vertex].add_neighbor(self.vertex_list[to_vertex], weight)

    def get_vertex(self,value):
        if value in self.vertex_list:
            return self.vertex_list[value]
        else:
            return None

    def get_vertices(self):
        return self.vertex_list.keys()

    def __iter__(self):
        return iter(self.vertex_list.values())

    def __contains__(self, value):
        return value in self.vertex_list

'''
g = graph()
for i in range(10):
    g.add_vertex(i)

print("Vertex List:")
print(g.vertex_list)
print()

import random
for i in range(10):
    g.add_edge(i, i+1, random.randint(0,10))

for vertex in g:
    print(vertex)
    print(vertex.get_connections())
    print()
'''
