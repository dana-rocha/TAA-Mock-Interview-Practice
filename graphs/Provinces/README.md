Replit link: https://replit.com/@dana-rocha/graphs-practice-1

Lesson: Graphs Part 1
Date: 10/13/22

# Number of Provinces

You are given an undirected graph with `N` nodes. Each node represents a city. Two cities `a` and `b` belong to a single _province_ if there is a possible path from `a` to `b` or vice versa.

Paths from `a` to `b` through intermediary cities such as a city `c` are valid paths. 

You are given the graph as an adjacency matrix `is_connected` where `is_connected[i][j] = 1` indicates that cities `i` and `j` are directly connected. Otherwise `is_connected[i][j] = 0` even if there is an indirect path from `i` to `j`. 

Return the total number of provinces in `is_connected`. 

## Example 1

*Input:*
```py
is_connected = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]
```
*Output:* 2

![example one graph](./images/example_one_two.png)


## Example 2
*Input:*
```py
is_connected = [
    [0, 0, 1],
    [0, 0, 0],
    [1, 0, 0]
]
```

*Output*: 2

![example two graph](./images/example_one_two.png)


## Example 3

*Input:*
```py
is_connected = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
```
*Output:* 3

![example three graph](./images/example_three.png)


Adapted from: [https://leetcode.com/problems/number-of-provinces](https://leetcode.com/problems/number-of-provinces)

