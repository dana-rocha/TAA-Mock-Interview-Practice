import pytest
from binary_search_trees.bfs import Tree, TreeNode


class TreeExtended(Tree):

    def add_helper(self, current_node, new_node):
        if new_node.key < current_node.key:
            if not current_node.left:
                current_node.left = new_node
                return
            self.add_helper(current_node.left, new_node)
        else:
            if not current_node.right:
                current_node.right = new_node
                return
            self.add_helper(current_node.right, new_node)

    def add(self, key, value=None):
        if not self.root:
            self.root = TreeNode(key, value)
        else:
            new_node = TreeNode(key, value)
            self.add_helper(self.root, new_node)


@pytest.fixture()
def empty_tree() -> TreeExtended():
    return TreeExtended()


@pytest.fixture()
def tree_with_nodes(empty_tree) -> TreeExtended():
    empty_tree.add(5, "Peter")
    empty_tree.add(3, "Paul")
    empty_tree.add(1, "Mary")
    empty_tree.add(10, "Karla")
    empty_tree.add(15, "Ada")
    empty_tree.add(25, "Kari")

    return empty_tree


def test_bfs(tree_with_nodes):

    expected_answer = ["Peter", "Paul", "Karla", "Mary", "Ada", "Kari"]

    answer = tree_with_nodes.bfs()
    assert answer == expected_answer



