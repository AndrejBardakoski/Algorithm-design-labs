n, m, k = [int(inp) for inp in input().split()]
capitals = [int(inp) - 1 for inp in input().split()]

union_find = []  # represent the parent of i-th node
for i in range(n):
    union_find.append(i)  # initially every node is a parent to itself
sz = [1] * n  # represent the size of the tree where the i-th node is the root
wh = [0] * n  # represent the total number of edges in the graph where the i-th node is the root


def findRoot(a):
    root_a = a
    while union_find[root_a] != root_a:
        root_a = union_find[root_a]
    while a != root_a:
        tmp = union_find[a]
        union_find[a] = root_a
        a = tmp
    return root_a


def addEdge(x, y):
    root_x = findRoot(x)
    root_y = findRoot(y)

    if root_x != root_y:
        if sz[root_x] < sz[root_y]:
            union_find[root_x] = root_y
            sz[root_y] += sz[root_x]
            wh[root_y] += wh[root_x] + 1
        else:
            union_find[root_y] = root_x
            sz[root_x] += sz[root_y]
            wh[root_x] += wh[root_y] + 1
    else:
        wh[root_x] += 1


for edge in range(m):
    a, b = [int(x) for x in input().split()]
    addEdge(a - 1, b - 1)

roots = []

# find all roots
for i in range(n):
    if union_find[i] == i:
        roots.append(i)

capital_roots = []
size_max = 0
capital_root_max = -1
# find all capital roots and the biggest tree containing capital
for capital in capitals:
    root = findRoot(capital)
    capital_roots.append(root)
    size = sz[root]
    if size > size_max:
        size_max = size
        capital_root_max = root

for root in capital_roots:
    if root != capital_root_max:
        roots.remove(root)

missing_edges = 0
n_edges = 0
full_size = 0

for root in roots:
    n_edges += wh[root]
    full_size += sz[root]

max_edges = (full_size * (full_size - 1)) // 2
missing_edges += max_edges - n_edges

for root in capital_roots:
    if root != capital_root_max:
        max_edges = (sz[root] * (sz[root] - 1)) // 2
        missing_edges += max_edges - wh[root]

print(missing_edges)
