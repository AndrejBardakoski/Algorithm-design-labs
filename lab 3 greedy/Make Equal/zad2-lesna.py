test_num = int(input())

for test in range(test_num):
    n = int(input())
    A = []
    sumA = 0
    sum_temp = 0
    flag = True

    line = input()
    line_split = line.split()
    for i in range(n):
        A.append(int(line_split[i]))

    for i in range(n):
        sumA += A[i]

    if not (sumA % n == 0):
        print("NO")
        continue

    desiredState = sumA / n

    A.reverse()

    for i in range(n):
        sum_temp += A[i]
        if sum_temp > (i + 1) * desiredState:
            flag = False
            break

    if (flag):
        print("YES")
    else:
        print("NO")
