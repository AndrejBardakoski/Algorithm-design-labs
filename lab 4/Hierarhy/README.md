# Hierarchy

Nick's company employed `n` people. Now Nick needs to build a tree hierarchy of «supervisor-surbodinate» relations in
the company (this is to say that each employee, except one, has exactly one supervisor). There are `m` applications
written in the following form: «employee `a_i` is ready to become a supervisor of employee `b_i` at extra cost `c_i`».
The qualification `q_j` of each employee is known, and for each application the following is true: `q_ai > q_bi`.

Would you help Nick calculate the minimum cost of such a hierarchy, or find out that it is impossible to build it.

### Input

The first input line contains integer `n` `(1 ≤ n ≤ 1000)` — amount of employees in the company. The following line
contains n space-separated numbers `q_j` `(0 ≤ qj ≤ 10^6)`— the employees' qualifications. The following line contains
number `m` `(0 ≤ m ≤ 10000)` — amount of received applications. The following `m` lines contain the applications
themselves, each of them in the form of three space-separated numbers: `a_i`, `b_i`
and `c_i` `(1 ≤ ai, bi ≤ n, 0 ≤ ci ≤ 10^6)`. Different applications can be similar, i.e. they can come from one and the
same employee who offered to become a supervisor of the same person but at a different cost. For each
application `q_ai > q_bi`.

### Output

Output the only line — the minimum cost of building such a hierarchy, or `-1` if it is impossible to build it.

### Sample 1

| input                                                  | result |
|--------------------------------------------------------|--------|
| 4<br>7 2 3 1<br>4<br>1 2 5<br>2 4 1<br>3 4 1<br>1 3 5  | 11     |

### Sample 2

| input                               | result |
|-------------------------------------|--------|
| 3<br>1 2 3<br>2<br>3 1 2<br>3 1 3   | -1     |

### Note

In the first sample one of the possible ways for building a hierarchy is to take applications with indexes `1`, `2`
and `4`, which give `11` as the minimum total cost. In the second sample it is impossible to build the required
hierarchy, so the answer is `-1`.