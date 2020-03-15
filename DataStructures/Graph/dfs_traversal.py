from DataStructures.Graph.Graph import Graph


def dfs_traversal(graph, source):
    """
    Time Complexity: O(V + E)
    """
    result = []
    visited = set()

    # Add the source vertex to the stack
    stack = [source]

    while len(stack) > 0:
        vertex = stack.pop()
        result.append(vertex)
        visited.add(vertex)

        if vertex in graph.adjacency_list:
            adjacency_list_of_vertex = graph.adjacency_list[vertex]
            head = adjacency_list_of_vertex.get_head()

            current_node = head
            while current_node is not None:
                child_vertex = current_node.data

                # Append to the stack if the child vertex is not already visited
                if child_vertex not in visited:
                    stack.append(child_vertex)

                current_node = current_node.next

    return result


g = Graph(6)
g.add_edges([[1, 2], [1, 3], [2, 4], [2, 5], [3, 6]])
g.print_graph()

traversed_list = dfs_traversal(g, source=1)
print(traversed_list)

