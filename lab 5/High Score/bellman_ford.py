import sys

input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
neighbours = [[] for x in range(n)]
for i in range(m):
    a, b, c = [int(x) for x in input().split()]
    a -= 1
    b -= 1
    c *= -1
    neighbours[a].append([b, c])

dist = [1e18] * n
negative_c = [False] * n
visited = [False] * n

visited[0] = True
dist[0] = 0

for i in range(n):
    for ind in range(n):
        if not visited[ind]:
            continue
        for neighbor, cost in neighbours[ind]:
            new_dist = dist[ind] + cost
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                visited[neighbor] = True

n_dist = dist

for i in range(n):
    for ind in range(n):
        if not visited[ind]:
            continue
        for neighbor, cost in neighbours[ind]:
            new_dist = dist[ind] + cost
            if new_dist < dist[neighbor]:
                n_dist[neighbor] = -1e18
                negative_c[neighbor] = True

if negative_c[n - 1]:
    print(-1)
else:
    print(-dist[n - 1])
