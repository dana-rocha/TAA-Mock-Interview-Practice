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
    if not root:
        return -1

    q = deque([root])

    curr_level = 0
    max_level = 0
    max = 0

    while q:
        width = len(q)

        if max < width:
            max = width
            max_level = curr_level

        while width > 0:
            curr = q.popleft()

            width = width - 1

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        curr_level += 1

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