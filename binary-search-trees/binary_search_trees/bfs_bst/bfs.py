'''
Lesson: Binary Search Trees
Date: 9/22/22

https://replit.com/@adadev/bst-dfs-practice#binary_search_trees/bfs.py
'''

class TreeNode:

    def __init__(self, key, value=None, left=None, right=None):
        if not value:
            value = key
        self.key = key
        self.val = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode {self.val}"


class Tree:

    def __init__(self):
        self.root = None

    def bfs(self):
        pass
