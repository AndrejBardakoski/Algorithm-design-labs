case = 0
while True:
    case += 1
    n = int(input())
    if n == 0:
        break

    courencies = {}
    for i in range(n):
        s = input()
        courencies[s] = i

    m = int(input())
    matrix = [[0] * n for x in range(n)]
    for i in range(n):
        matrix[i][i] = 1
    for i in range(m):
        s = input().split()
        a = courencies[s[0]]
        b = courencies[s[2]]
        c = float(s[1])
        if (a == b) and c < 0:
            continue
        matrix[a][b] = c
    input()

    for q in range(n):
        for i in range(n):
            for j in range(n):
                new_w = matrix[i][q] * matrix[q][j]
                if new_w > matrix[i][j]:
                    matrix[i][j] = new_w

    valid = True
    for i in range(n):
        if matrix[i][i] > 1:
            valid = False

    if valid:
        print("Case " + str(case) + ": No")
    else:
        print("Case " + str(case) + ": Yes")
