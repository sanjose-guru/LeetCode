# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) != -1

    def dfs(self, root: Optional[TreeNode]) -> int:
        # base case.
        if root == None:
            return 0

        lh = self.dfs(root.left)
        rh = self.dfs(root.right)

        # if the left or right child is unbalanced
        if lh == -1 or rh == -1:
            return -1

        # if the child height diff i more than 1, it is unbalanced.
        if abs(lh - rh) > 1:
            return -1

        # return height of the tree so far.
        return max(lh, rh) + 1
