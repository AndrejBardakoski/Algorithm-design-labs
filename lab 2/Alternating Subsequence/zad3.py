nTests = int(input())

for testIter in range(nTests):

    n = int(input())
    A = [int(x) for x in input().split()]

    sum_ = 0
    max_ = A[0]

    for i in range(1, n):
        if (A[i - 1] < 0 < A[i]) or (A[i - 1] > 0 > A[i]):
            sum_ += max_
            max_ = A[i]
        elif A[i] > max_:
            max_ = A[i]

    sum_ += max_
    print(sum_)
