from DataStructures.Graph import Graph

directed_graph_1 = Graph(4, True)
directed_graph_1.add_edges([[0, 1], [0, 1], [0, 2], [1, 3], [2, 3]])
directed_graph_1.print_graph()
