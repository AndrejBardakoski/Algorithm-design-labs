import heapq as hq
import sys

input = sys.stdin.readline


def dijkstra(start, nbrs):
    n = len(nbrs)
    distances = [1e18] * n
    distances[start] = 0
    pq = [(0, start)]
    hq.heapify(pq)

    while len(pq) > 0:
        dist_current, index_current = hq.heappop(pq)
        if distances[index_current] < dist_current:
            continue
        for nbr_index, nbr_cost in nbrs[index_current]:
            new_nbr_cost = nbr_cost + dist_current
            if new_nbr_cost < distances[nbr_index]:
                distances[nbr_index] = new_nbr_cost
                hq.heappush(pq, (new_nbr_cost, nbr_index))

    return distances


n, m = (int(x) for x in input().split())

neighbours = [[] for x in range(n)]
for i in range(m):
    a, b, c = (int(x) for x in input().split())
    a -= 1
    b -= 1
    neighbours[a].append([b, c])

result_distances = dijkstra(0, neighbours)
print(" ".join(map(str, result_distances)))
