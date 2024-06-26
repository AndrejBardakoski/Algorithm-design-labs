# Alternating Subsequence - *task3*

Recall that the sequence `b` is a subsequence of the sequence `a` if `b` can be derived from `a`
by removing zero or more elements without changing the order of the remaining elements. For example, if
`a=[1,2,1,3,1,2,1]`, then possible subsequences are: `[1,1,1,1]`, `[3]` and `[1,2,1,3,1,2,1]`, but not `[3,2,3]`
and `[1,1,1,1,2]`.

You are given a sequence `a` consisting of `n` positive and negative elements (there is no zeros in the sequence).

Your task is to choose maximum by size (length) alternating subsequence of the given sequence (i.e. the sign of each
next element is the opposite from the sign of the current element, like positive-negative-positive and so on or
negative-positive-negative and so on). Among all such subsequences, you have to choose one which has the maximum sum of
elements.

In other words, if the maximum length of alternating subsequence is `k` then your task is to find the maximum sum of
elements of some alternating subsequence of length `k`.

You have to answer `t` independent test cases.

### Input

The first line of the input contains one integer `t` `(1≤t≤10&4)` — the number of test cases. Then `t` test cases
follow.

The first line of the test case contains one integer `n` `(1≤n≤2⋅10^5)` — the number of elements in `a`. The second line
of the test case contains `n` integers `a1,a2,…,an` `(−10^9≤ai≤10^9,ai≠0)`, where `a_i` is the `i-th` element of `a`.

It is guaranteed that the sum of `n` over all test cases does not exceed `2⋅10^5`
`(∑n≤2⋅10^5)`.

### Output

For each test case, print the answer — the maximum sum of the maximum by size (length) alternating subsequence of `a`.

### Sample 1

| input                                                                                                                          | result                      |
|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| 4<br>5<br>1 2 3 -1 -2<br>4<br>-1 -2 -1 -3<br>10<br>-2 8 3 8 -4 -15 5 -2 -3 1<br>6<br>1 -1000000000 1 -1000000000 1 -1000000000 | 2<br>-1<br>6<br>-2999999997 | 

### Note

In the first test case of the example, one of the possible answers is [1,2,<u>**3**</u>,<u>**-1**</u>,−2].

In the second test case of the example, one of the possible answers is [−1,−2,<u>**−1**</u>,−3].

In the third test case of the example, one of the possible answers is 
[<u>**−2**</u>,8,3,<u>**8**</u>,<u>**−4**</u>,−15,<u>**5**</u>,<u>**−2**</u>,−3,<u>**1**</u>].