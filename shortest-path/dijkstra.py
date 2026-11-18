import heapq
from math import inf


def dijkstra(graph, start):
    """Return shortest distances and predecessors from start.

    Edge weights must be non-negative.
    """
    distances = {node: inf for node in graph}
    distances[start] = 0
    predecessors = {}

    # The counter prevents comparisons between nodes when distances tie.
    from itertools import count
    counter = count()
    queue = [(0, next(counter), start)]

    while queue:
        distance, _, node = heapq.heappop(queue)

        if distance > distances[node]:
            continue  # Skip an outdated queue entry.

        for neighbor, weight in graph.get(node, []):
            if weight < 0:
                raise ValueError("Dijkstra's algorithm requires non-negative weights")

            new_distance = distance + weight
            if new_distance < distances.get(neighbor, inf):
                distances[neighbor] = new_distance
                predecessors[neighbor] = node
                heapq.heappush(queue, (new_distance, next(counter), neighbor))

    return distances, predecessors


def reconstruct_path(predecessors, start, target):
    """Return the shortest path, or None if the target is unreachable."""
    path = [target]
    while path[-1] != start:
        if path[-1] not in predecessors:
            return None
        path.append(predecessors[path[-1]])
    return path[::-1]


graph = {
    "A": [("B", 4), ("C", 1)],
    "B": [("D", 1)],
    "C": [("B", 2), ("D", 5)],
    "D": [],
}

distances, predecessors = dijkstra(graph, "A")
print(distances)  # {'A': 0, 'B': 3, 'C': 1, 'D': 4}
print(reconstruct_path(predecessors, "A", "D"))  # ['A', 'C', 'B', 'D']
