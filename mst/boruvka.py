def boruvka(n, edges):
    # Union-Find data structure
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if root_x == root_y:
            return False

        if rank[root_x] < rank[root_y]:
            root_x, root_y = root_y, root_x

        parent[root_y] = root_x

        if rank[root_x] == rank[root_y]:
            rank[root_x] += 1

        return True

    mst = []
    mst_weight = 0
    num_components = n

    while num_components > 1:
        # Cheapest outgoing edge for each component
        cheapest = [None] * n

        for u, v, weight in edges:
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                continue

            if cheapest[root_u] is None or weight < cheapest[root_u][2]:
                cheapest[root_u] = (u, v, weight)

            if cheapest[root_v] is None or weight < cheapest[root_v][2]:
                cheapest[root_v] = (u, v, weight)

        # Add the cheapest edges to the MST
        for edge in cheapest:
            if edge is None:
                continue

            u, v, weight = edge

            if union(u, v):
                mst.append(edge)
                mst_weight += weight
                num_components -= 1

    return mst, mst_weight


n = 4

edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst, weight = boruvka(n, edges)

print("MST:")
for u, v, w in mst:
    print(f"{u} -- {v}: {w}")

print("Total weight:", weight)
