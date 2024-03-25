test_num = int(input())

for test in range(test_num):
    n = int(input())
    A = []

    line = input()
    line_split = line.split()
    for i in range(n):
        A.append(int(line_split[i]))

    i = 1
    for item in A:
        if (item == i):
            i += 1
        i += 1

    print(i - 1)
