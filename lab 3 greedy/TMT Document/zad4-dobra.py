test_num = int(input())
for test in range(test_num):
    length = int(input())
    string = input()

    n = length / 3

    counterT1 = 0
    counterM = 0
    counterT2 = 0

    for c in string:
        if c == 'T':
            if counterT1 < n:
                counterT1 += 1
            else:
                counterT2 += 1
        if c == 'M':
            counterM += 1

        if counterM > counterT1 or counterT2 > counterM:
            break

    if counterT1 == counterM == counterT2 == n:
        print("YES")
    else:
        print("NO")
