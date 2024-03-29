import sys
input = sys.stdin.readline
n, m, q = [int(inp) for inp in input().split()]

matrix = []
for i in range(n):
    row = [-1] * m
    matrix.append(row)

nVer = 0
ver_coords = []
for i in range(n):
    row = input()
    for j in range(m):
        if row[j] == '.':
            matrix[i][j] = nVer
            nVer += 1
            ver_coords.append([i, j])

union_find = []  # represent the parent of i-th node
wh = [0] * nVer  # represent the total number of pictures in the tree where the i-th node is the root
sz = [1] * nVer  # represent the size of the tree where the i-th node is the root
for i in range(nVer):
    union_find.append(i)

for coord in ver_coords:
    i, j = coord
    a = matrix[i][j]
    weight = 0
    a_up = matrix[i - 1][j]
    a_d = matrix[i + 1][j]
    a_r = matrix[i][j + 1]
    a_l = matrix[i][j - 1]
    if a_up == -1:
        weight += 1
    if a_d == -1:
        weight += 1
    if a_r == -1:
        weight += 1
    if a_l == -1:
        weight += 1
    wh[a] = weight


def findRoot(a):
    root_a = a
    while union_find[root_a] != root_a:
        union_find[root_a] = union_find[union_find[root_a]]
        root_a = union_find[root_a]
    return root_a


def addEdge(x, y):
    root_x = findRoot(x)
    root_y = findRoot(y)

    if root_x != root_y:
        if sz[root_x] < sz[root_y]:
            union_find[root_x] = root_y
            sz[root_y] += sz[root_x]
            wh[root_y] += wh[root_x]
        else:
            union_find[root_y] = root_x
            sz[root_x] += sz[root_y]
            wh[root_x] += wh[root_y]


for coord in ver_coords:
    i, j = coord
    a = matrix[i][j]
    a_up = matrix[i - 1][j]
    a_d = matrix[i + 1][j]
    a_r = matrix[i][j + 1]
    a_l = matrix[i][j - 1]
    if a_up > -1:
        addEdge(a, a_up)
    if a_d > -1:
        addEdge(a, a_d)
    if a_r > -1:
        addEdge(a, a_r)
    if a_l > -1:
        addEdge(a, a_l)

for i in range(nVer):
    root = findRoot(i)
    wh[i] = wh[root]

for test in range(q):
    cord_x, cord_y = [int(inp) for inp in input().split()]
    vert = matrix[cord_x - 1][cord_y - 1]
    print(wh[vert])
