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

    def inorder_helper(self, current_node, values):
        if not current_node:
            return values

        self.inorder_helper(current_node.left, values)
        values.append({"key": current_node.key, "value": current_node.val})
        self.inorder_helper(current_node.right, values)

        return values

    def inorder(self):
        values = []
        return self.inorder_helper(self.root, values)

    def preorder_helper(self, current_node, values):
        if not current_node:
            return values

        values.append({ 
            "key": current_node.key,
            "value": current_node.val
        })
        self.preorder_helper(current_node.left, values)        
        self.preorder_helper(current_node.right, values)

        return values

    def preorder(self):
        values = []
        return self.preorder_helper(self.root, values)

    def postorder_helper(self, current_node, values):
        if not current_node:
            return values

        self.postorder_helper(current_node.left, values)        
        self.postorder_helper(current_node.right, values)
        values.append({ 
            "key": current_node.key,
            "value": current_node.val
        })

        return values

    def postorder(self):
        values = []
        return self.postorder_helper(self.root, values)
