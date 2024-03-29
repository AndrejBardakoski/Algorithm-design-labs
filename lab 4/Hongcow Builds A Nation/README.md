# Hongcow Builds A Nation

Hongcow is ruler of the world. As ruler of the world, he wants to make it easier for people to travel by road within
their own countries.

The world can be modeled as an undirected graph with `n` nodes and `m` edges. `k` of the nodes are home to the
governments of the `k` countries that make up the world.

There is at most one edge connecting any two nodes and no edge connects a node to itself. Furthermore, for any two nodes
corresponding to governments, there is no path between those two nodes. Any graph that satisfies all of these conditions
is stable.

Hongcow wants to add as many edges as possible to the graph while keeping it stable. Determine the maximum number of
edges Hongcow can add.

### Input

The first line of input will contain three integers `n`, `m` and `k` `(1 ≤ n ≤ 1 000, 0 ≤ m ≤ 100 000, 1 ≤ k ≤ n)` — the
number of vertices and edges in the graph, and the number of vertices that are homes of the government.

The next line of input will contain `k` integers `c1, c2, ..., ck (1 ≤ ci ≤ n)`. These integers will be pairwise
distinct and denote the nodes that are home to the governments in this world.

The following `m` lines of input will contain two integers `u_i` and `v_i` `(1 ≤ u_i, v_i ≤ n)`. This denotes an
undirected edge between nodes `u_i` and `v_i`.

It is guaranteed that the graph described by the input is stable.

### Output

Output a single integer, the maximum number of edges Hongcow can add to the graph while keeping it stable.

### Sample 1

| input                 | result |
|-----------------------|-------|
| 4 1 2<br>1 3<br>1 2   | 2     |

### Sample 2

| input                           | result |
|---------------------------------|--------|
| 3 3 1<br>2<br>1 2<br>1 3<br>2 3 | 0      |
