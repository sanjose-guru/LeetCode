# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isBst(r: TreeNode, min_val, max_val: float) -> bool:
            if not r:
                return True

            if not (min_val < r.val < max_val):
                return False

            return isBst(r.left, min_val, r.val) and isBst(r.right, r.val, max_val)

        # check if this is a BST
        return isBst(root, -float("inf"), float("inf"))
