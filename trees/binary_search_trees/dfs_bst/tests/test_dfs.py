import pytest
from dfs_bst.dfs import Tree, TreeNode


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


def test_inorder_with_empty_tree(empty_tree):
    assert empty_tree.inorder() == []


def test_inorder_with_nodes(tree_with_nodes):
    expected_answer = [{
        "key": 1,
        "value": "Mary"
    }, {
        "key": 3,
        "value": "Paul"
    }, {
        "key": 5,
        "value": "Peter"
    }, {
        "key": 10,
        "value": "Karla"
    }, {
        "key": 15,
        "value": "Ada"
    }, {
        "key": 25,
        "value": "Kari"
    }]

    answer = tree_with_nodes.inorder()
    assert answer == expected_answer


def test_preorder_on_empty_tree(empty_tree):
    assert empty_tree.preorder() == []


def test_preorder_on_tree_with_nodes(tree_with_nodes):
    expected_answer = [{
        "key": 5,
        "value": "Peter"
    }, {
        "key": 3,
        "value": "Paul"
    }, {
        "key": 1,
        "value": "Mary"
    }, {
        "key": 10,
        "value": "Karla"
    }, {
        "key": 15,
        "value": "Ada"
    }, {
        "key": 25,
        "value": "Kari"
    }]

    answer = tree_with_nodes.preorder()
    assert answer == expected_answer


def test_postorder_on_empty_tree(empty_tree):
    assert empty_tree.postorder() == []


def test_postorder_on_tree_with_nodes(tree_with_nodes):
    expected_answer = [{
        "key": 1,
        "value": "Mary"
    }, {
        "key": 3,
        "value": "Paul"
    }, {
        "key": 25,
        "value": "Kari"
    }, {
        "key": 15,
        "value": "Ada"
    }, {
        "key": 10,
        "value": "Karla"
    }, {
        "key": 5,
        "value": "Peter"
    }]

    answer = tree_with_nodes.postorder()
    assert answer == expected_answer
