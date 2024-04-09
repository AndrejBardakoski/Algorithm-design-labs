# Shortest Routes I

There are `n` cities and `m` roads between them. Your task is to process `q` queries where you have to determine the
length of the shortest route between two given cities.

### Input

The first input line has three integers `n`, `m` and `q`: the number of cities, roads, and queries.

Then, there are `m` lines describing the roads. Each line has three integers `a`, `b` and `c`: there is a road between
cities `a` and `b` whose length is `c`. All roads are two-way roads.

Finally, there are `q` lines describing the queries. Each line has two integers `a` and `b`: determine the length of the
shortest route between cities `a` and `b`.

### Output

Print the length of the shortest route for each query. If there is no route, print `−1` instead.

### Sample 1

| input                                                               | result                  |
|---------------------------------------------------------------------|-------------------------|
| 4 3 5<br>1 2 5<br>1 3 9<br>2 3 3<br>1 2<br>2 1<br>1 3<br>1 4<br>3 2 | 5<br>5<br>8<br>-1<br>3  |
