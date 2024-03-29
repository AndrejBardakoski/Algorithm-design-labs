n = int(input())
input()
m = int(input())

min_costs = [-1] * n

for q in range(m):
    supervisor, subordinate, cost = [int(x) for x in input().split()]
    supervisor -= 1
    subordinate -= 1
    if min_costs[subordinate] == -1:
        min_costs[subordinate] = cost
    elif min_costs[subordinate] > cost:
        min_costs[subordinate] = cost

sum_cost = 0
without_supervisor = 0
for cost in min_costs:
    if cost == -1:
        without_supervisor += 1
    else:
        sum_cost += cost

if without_supervisor > 1:
    print(-1)
else:
    print(sum_cost)
