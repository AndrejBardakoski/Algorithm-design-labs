test_num = int(input())
ranks = [0, 9, 17, 24, 30, 35, 39, 42, 44, 45]

for test in range(test_num):
    n = int(input())

    for i in range(1, 10):
        if n <= ranks[i]:
            output = (n - ranks[i - 1]) * 10 ** (i - 1)
            for j in range(0, i - 1):
                output += (9 - j) * 10 ** j
            print(output)
            break
