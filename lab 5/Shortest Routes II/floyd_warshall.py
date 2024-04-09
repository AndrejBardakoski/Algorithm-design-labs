import sys
input = sys.stdin.readline

n, m, q = [int(x) for x in input().split()]
dist = [[1e18] * n for x in range(n)]
for i in range(n):
    dist[i][i] = 0

for i in range(m):
    a, b, c = [int(x) for x in input().split()]
    a -= 1
    b -= 1
    dist[a][b] = min(dist[a][b], c)
    dist[b][a] = min(dist[b][a], c)

for iter in range(n):
    for i in range(n):
        for j in range(n):
            new_dist = dist[i][iter] + dist[iter][j]
            dist[i][j] = min(dist[i][j], new_dist)

for i in range(n):
    for j in range(n):
        if dist[i][j] == 1e18:
            dist[i][j] = -1

for i in range(q):
    a, b = [int(x) for x in input().split()]
    a -= 1
    b -= 1
    print(dist[a][b])
