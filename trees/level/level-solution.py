'''
We are interested in writing a function that returns which level in a binary tree has the most nodes. The root of the tree is considered level 0. 

Our function should accept one argument, the root of the binary tree and return an integer representing the level of the tree with the most nodes. 

For example, given the root of this tree:

Level 0:             1
                   /    \
                  /      \
Level 1:         2        3
               /   \    /   \
Level 2:      4     5  6     7
             / \      /     
Level 3:    8   9    10 

The function should return 2 because level 2 has 4 nodes (4, 5, 6, 7) which is more than any of the other levels.

If the tree is empty, return -1. 
'''


# DO NOT MODIFY THE NODE CLASS
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# import deque
from collections import deque


def level(root):

    # return -1 if the tree is empty
    if not root:
        return -1

    #create a new queue
    q = deque()

    # add the root to the queue
    q.append(root)

    # track current level we are iterating over
    curr_level = 0
    # track level with max number of nodes so far
    max_level = 0
    # track max number of nodes in a level so far
    max = 0

    # loop until the queue is empty
    while q:

        # calculate the total number of nodes 
        # in the current level
        width = len(q)

        # if more nodes in current level
        # than any level traversed so far
        if max < width:
            # set maximum number of nodes in a level 
            # to number of nodes in current level
            max = width
            # set level with maximum number of nodes
            # to current level
            max_level = curr_level

        # while there are nodes we haven't traversed
        # in current level
        while width > 0:
            # pop next node in level off the queue
            curr = q.popleft()
            
            # subtract one from width
            width = width - 1

            # if popped node has a left child
            if curr.left:
                # add child to the queue
                q.append(curr.left)

            # if popped node has a right child
            if curr.right:
                # add child to the queue
                q.append(curr.right)
        # increment our current level
        curr_level += 1
    # return level with most nodes
    return max_level

    
'''          1
           /    \
          /      \
         2        3
       /   \    /   \
      4     5  6     7
     / \      / \    
    8   9    10 11
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
assert level(root) == 2

''' 
    1
'''
root = Node(1)
assert level(root) == 0

'''
             1
           /    \
          /      \
         2        3
       /   \  
      4     5 
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
assert level(root) == 1

'''
    Empty Tree
'''
root = None
assert level(root) == -1


print("All tests passed! If time remains discuss time and space complexity")

'''
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------

Q: Is the tree a binary search tree?
A: The tree is a binary tree but may not be a binary _search_ tree. 

Q: Can two levels have the same number of nodes?
A: Yes. In the case of a tie, return the smaller level. For example, if both levels 2 and 3 have 4 nodes each, return level 2. See test case 3.

Q: What should I do if invalid input is passed in?
A: You can assume that the input will be valid.

Q: What data types will be stored in the values?
A: Integers.

Q: Will the tree be balanced?
A: The tree will not necessarily be balanced. 

--------------------------------------------------



---------Hints for struggling candidates----------

 - If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper. 

 - If your candidate still struggles, ask them how they would like to traverse the tree using pen and paper. Does the order in which they process the nodes matter? As a further hint, how can we traverse the tree by level? (BFS)

 - If your candidate still struggles, suggest that they first try and return the number of nodes in the level with the most nodes. For instance, for the introductory example return 4 (the number of nodes in level 2), instead of 2 (the level). Then incorporate tracking the levels.
 
 - It can be challenging to debug this problem. If your candidate is failing a test and unsure why, encourage them to add print statements that help them see what nodes are being visited when. 
 
 -------------------------------------------------

OPTIONAL BONUS AT-HOME CHALLENGES (after interview):

- What are the time/space complexities of the sample solution? Does it make a difference whether the tree is balanced or not?

- If you wrote a Breadth First Search (level-order) solution, try writing a Depth First Search solution. 
'''