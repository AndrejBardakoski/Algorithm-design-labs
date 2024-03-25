line = input()
line_split = line.split()
n = int(line_split[0])
m = int(line_split[1])
k = int(line_split[2])

A = []
line = input()
line_split = line.split()
for i in range(n):
    A.append(int(line_split[i]))

o_per_d = n // 2 + 1  # num of operations required for 1 diamond
d_per_m = m // o_per_d  # num of diamonds per min

if (n % 2 == 0):
    print(0)
elif (d_per_m == 0):
    print(0)
else:
    minA = min(A[::2])
    print(min(minA, int(d_per_m * k)))
