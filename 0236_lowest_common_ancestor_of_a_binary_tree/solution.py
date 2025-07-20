# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Base case
        # If we hit a deadend or if we hit one of the values stop going down further.
        if not root or root.val == p.val or root.val == q.val:
            return root

        # Check if our value exists on left/right side.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if we got non null for left and right we are an ancestor.
        if left and right:
            return root
        # only left/right we found one of the value, just bubble up that node
        elif left:
            return left
        elif right:
            return right
        # the values are not found on this side of the tree
        else:
            return None
