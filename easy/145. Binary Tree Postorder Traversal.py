# Given the root of a binary tree, return the postorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        tree_values = list()
        if root is None:
            return tree_values
        tree_values += self.postorderTraversal(root.left)
        tree_values += self.postorderTraversal(root.right)
        tree_values.append(root.val)

        return tree_values
