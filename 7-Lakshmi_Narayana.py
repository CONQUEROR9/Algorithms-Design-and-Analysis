adjacency_matrix = [[0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 1],
                    [0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0]
                    ]


def bfs(adj_matrix):
    visited = set()
    for row in range(len(adj_matrix)):
        for col in range(len(adj_matrix[0])):
            if (row, col) not in visited:
                nodes = [(row, col)]
                while nodes:
                    row, col = nodes.pop(0)
                    if row >= len(adj_matrix) or col >= len(adj_matrix[0]) or row < 0 or col < 0:
                        continue
                    if (row, col) not in visited:
                        if adj_matrix[row][col] == 1:
                            visited.add((row, col))
                            nodes.append((row + 1, col))
                            nodes.append((row, col + 1))
                            nodes.append((row - 1, col))
                            nodes.append((row, col - 1))
    print(visited)


bfs(adjacency_matrix)
