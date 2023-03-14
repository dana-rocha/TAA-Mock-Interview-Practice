'''
There is a bi-directional (undirected) graph with n vertices, where each vertex is labeled from 0 to n - 1.

The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [uᵢ, vᵢ] denotes an edge between vertex uᵢ and vertex vᵢ. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers, n, source, and destination, return True if there is a valid path from source to destination, or False otherwise.

Example:

       0 ------ 1
        \      /
         \    /
          \  /
            2

Input: n = 3, edges = [[[0,1],[1,2],[2,0]]], source = 0, destination = 2
Output: True

There are two paths that exist between node 0 and node 2:
- 0 -> 2
- 0 -> 1 -> 2

Please note there is no need to store the path to the node. You are only required to return whether the path exists (True or False).
'''
from collections import defaultdict
from collections import deque

def validPath(n, edges, source, destination):
    # store all of the edges
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # initialize list for storing visited nodes
    visited = []
    # initalize queue for storing nodes to visit 
    queue = deque([source])

    # while the queue is not empty
    while queue:
        # pop the current node off the queue
        current = queue.popleft()
        # return True if the current node is the desired destination
        if current == destination:
            return True

        # add all of the current node's unvisited neighbors to the queue and visited list
        for next_node in graph[current]:
            if next_node not in visited:
                visited.append(next_node)
                queue.append(next_node)


    # if we get here and haven't found our destination node, return False as there doesn't exist a path from source to destination
    return False


'''
       0 ------ 1
        \      /
         \    /
          \  /
            2
'''
### Test Case #1

n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
dest = 2

assert validPath(n, edges, source, dest) == True

'''
   1            3
  /             | \
 /              |  \
0               |   5
 \              |  /
  \             | /
   2            4
'''
n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
dest = 5

assert validPath(n, edges, source, dest) == False

'''
   1 
  /
 /
0
 \ 
  \ 
   2
'''
n = 3
edges = [[0,1],[2,0]]
source = 2
dest = 1

assert validPath(n, edges, source, dest) == True

print("All tests passed! If time remains discuss time and space complexity")

'''
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------

Q: Is it guaranteed to be an undirected graph?
A: Yes, the graph is guaranted to be undirected. Meaning, if an edge exists from A to B, an edge also exists from B to A.

Q: Can a vertex have an edge to itself?
A: No. It is guaranteed that there are no self-edges in the graph.

Q: What should I do if invalid input is passed in?
A: You can assume that the input will be valid.

Q: Does the graph contain weighted edges?
A: No. The graph is unweighted.  

--------------------------------------------------


---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper. 

 - If your candidate still struggles, ask them how they would like to traverse the graph using pen and paper.

 - If your candidate still struggles, suggest them to consider implementing a solution with Breadth-First-Search or Depth-First-Search approach.
 
 - It can be challenging to debug this problem. If your candidate is failing a test and unsure why, encourage them to add print statements that help them see what nodes are being visited when. 
 
 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):

- What are the time/space complexities of the sample solution? 

- If you wrote a Breadth First Search solution, try writing a Depth First Search solution, and vice versa.
'''