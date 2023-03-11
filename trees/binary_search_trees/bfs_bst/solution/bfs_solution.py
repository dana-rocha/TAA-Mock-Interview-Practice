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
        if not self.root:
            return []

        queue = []
        visited = []

        queue.append(self.root)
        visited.append(self.root.val)

        while queue:
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
                visited.append(node.left.val)
            if node.right:
                queue.append(node.right)
                visited.append(node.right.val)
        return visited
