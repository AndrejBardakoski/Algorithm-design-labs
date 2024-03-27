num_test = int(input())
for test in range(num_test):
    n = int(input())
    A = [int(x) for x in input().split()]
    num_pairs = int(input())
    pairs = []
    for pair in range(num_pairs):
        pairs.append([int(x) for x in input().split()])

    B = [0]

    for i in range(0, n - 1):
        if A[i] == A[i + 1]:
            B.append(B[i])
        else:
            B.append(i+1)

    for pair in pairs:
        a, b = pair

        if B[a-1] == B[b-1]:
            print("-1 -1")
        else:
            print(str(B[b-1]) + " " + str(b))

    print()
