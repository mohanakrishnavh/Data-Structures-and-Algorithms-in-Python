def dynamic_array(n, queries):
    seq_list = []
    for i in range(n):
        seq_list.append([])
    query_size = len(queries)
    last_answer = 0

    for i in range(query_size):
        query_type = queries[i][0]
        x = queries[i][1]
        y = queries[i][2]

        if query_type == 1:
            expr = (x ^ last_answer) % n
            (seq_list[expr]).append(y)

        elif query_type == 2:
            expr = (x ^ last_answer) % n
            seq = seq_list[expr]
            size = len(seq)
            idx = y % size
            last_answer = seq[idx]
            print(last_answer)

        else:
            print("Incorrect Input Type")

'''
N = 2
QUERIES = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
dynamic_array(N, QUERIES)
'''
