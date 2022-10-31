from heapq import *
from collections import defaultdict


def prim():
    nodes = list("ABCDE")
    edges = [('A', 'B', 2), ('A', 'C', 2), ('A', 'D', 5), ('A', 'E', 3), ('B', 'A', 2), ('B', 'C', 1), ('B', 'D', 4),
             ('B', 'E', 4), ('C', 'A', 2), ('C', 'B', 1), ('C', 'D', 3), ('C', 'E', 5), ('D', 'A', 5), ('D', 'B', 4),
             ('D', 'C', 3), ('D', 'E', 9), ('E', 'A', 3), ('E', 'B', 4), ('E', 'C', 5), ('E', 'D', 9)]


    Q = defaultdict(list)
    for start_pos, end_pos, cost in edges:
        Q[start_pos].append((cost, start_pos, end_pos))
        Q[end_pos].append((cost, end_pos, start_pos))

    shortest_path = []
    visited = {nodes[0]}
    unvisited_edges = Q[nodes[0]][:]
    heapify(unvisited_edges)

    while unvisited_edges:
        cost, start_pos, end_pos = heappop(unvisited_edges)
        if end_pos not in visited:
            visited.add(end_pos)
            shortest_path.append((start_pos, end_pos, cost))

            for e in Q[end_pos]:
                if e[2] not in visited:
                    heappush(unvisited_edges, e)
    return shortest_path


print(prim())
