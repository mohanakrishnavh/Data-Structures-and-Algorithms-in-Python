from datastructures.graph.Graph import Graph
from collections import deque


def bfs_traversal(graph, source):
    """
    Time Complexity: O(V + E)
    """
    result = []
    traversal_queue = deque([source])

    while traversal_queue:
        # Pop the vertex from the queue & add it to the result
        current_vertex = traversal_queue.popleft()
        result.append(current_vertex)

        # Get the adjacency list of the vertex and iterate over it and add all its adjacent vertices to the queue
        if current_vertex in graph.adjacency_list:
            adjacency_list_of_current_node = graph.adjacency_list[current_vertex]
            head_node = adjacency_list_of_current_node.get_head()

            current_node = head_node
            while current_node is not None:
                traversal_queue.append(current_node.data)
                current_node = current_node.next

    return result


g = Graph(5)
g.add_edges([[0, 1], [0, 2], [1, 3], [1, 4]])
g.print_graph()

traversed_list = bfs_traversal(g, source=0)
print(traversed_list)

