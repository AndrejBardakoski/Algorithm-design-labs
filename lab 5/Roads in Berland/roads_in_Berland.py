import sys

input = sys.stdin.readline

n = int(input())
dist = [[] for x in range(n)]

for i in range(n):
    dist[i] = [int(x) for x in input().split()]

k = int(input())
new_roads = [[] for x in range(k)]
for i in range(k):
    a, b, c = [int(x) for x in input().split()]
    a -= 1
    b -= 1
    new_roads[i] = [a, b, c]

for a, b, c in new_roads:
    for i in range(n):
        for j in range(n):
            new_dist_1 = dist[i][a] + c + dist[b][j]
            new_dist_2 = dist[i][b] + c + dist[a][j]
            dist[i][j] = min(dist[i][j], new_dist_1, new_dist_2)

    s = 0
    for i in range(n):
        for j in range(i, n):
            s += dist[i][j]

    print(s)
