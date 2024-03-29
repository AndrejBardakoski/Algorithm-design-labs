n, q = [int(x) for x in input().split()]

id = []
sz = [1] * n
for i in range(n):
    id.append(i)


def findRoot(a):
    root = a
    while id[root] != root:
        root = id[root]
    while a != root:
        tmp = id[a]
        id[a] = root
        a = tmp
    return root


for query in range(q):
    o, a, b = [int(x) for x in input().split()]

    root_a = findRoot(a)
    root_b = findRoot(b)

    if o == 0:
        if sz[root_a] < sz[root_b]:
            id[root_a] = root_b
            sz[root_b] += sz[root_a]
        else:
            id[root_b] = root_a
            sz[root_a] += sz[root_b]

    if o == 1:
        if root_a == root_b:
            print(1)
        else:
            print(0)
