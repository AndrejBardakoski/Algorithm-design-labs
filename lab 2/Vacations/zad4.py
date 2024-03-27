n = int(input())
A = [int(x) for x in input().split()]

dp = [[0, 0, 0]]

for i in range(0, n):
    row = [0, 0, 0]
    row[0] = max(dp[i])
    if A[i] == 1 or A[i] == 3:
        row[1] = max(dp[i][0], dp[i][2]) + 1
    if A[i] == 2 or A[i] == 3:
        row[2] = max(dp[i][0], dp[i][1]) + 1
    dp.append(row)

print(n - max(dp[n]))
