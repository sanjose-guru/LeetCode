# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base cases
        if not root:
            return False

        # if we are similar trees or if a child is a subtree
        return (
            self.areTreesSimilar(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

    # Will check if 2 trees are same.
    def areTreesSimilar(self, root1, root2: Optional[TreeNode]) -> bool:
        # base cases
        #
        # if both none, we are similarTree
        if not root1 and not root2:
            return True

        # if only 1 is none we are not similar.
        if not root1 or not root2:
            return False

        # if root is equal and the children are also similar we are similarTree.
        return (
            root1.val == root2.val
            and self.areTreesSimilar(root1.left, root2.left)
            and self.areTreesSimilar(root1.right, root2.right)
        )
