# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if not root:
            return depth

        node_queue = deque([root])
        while node_queue:
            depth += 1
            for _ in range(len(node_queue)):
                node = node_queue.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
        return depth
