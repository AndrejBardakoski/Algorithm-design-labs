# High Score

You play a game consisting of `n` rooms and `m` tunnels. Your initial score is `0`, and each tunnel increases your score
by `x` where  `x` may be both positive or negative. You may go through a tunnel several times.

Your task is to walk from room `1` to room `n`. What is the maximum score you can get?

### Input

The first input line has two integers `n` and `m`: the number of rooms and tunnels. The rooms are numbered `1,2,…,n`.

Then, there are `m` lines describing the tunnels. Each line has three integers `a`,`b` and `x`: the tunnel starts at
room `a`, ends at room `b`, and it increases your score by `x`. All tunnels are one-way tunnels.

You can assume that it is possible to get from room `1` to room `n`.

### Output

Print one integer: the maximum score you can get. However, if you can get an arbitrarily large score, print `−1`.

### Sample 1

| input                                               | result |
|-----------------------------------------------------|--------|
| 4 5<br>1 2 3<br>2 4 -1<br>1 3 -2<br>3 4 7<br>1 4 4  | 5      |
