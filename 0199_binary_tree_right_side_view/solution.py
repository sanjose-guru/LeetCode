# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        node_queue = deque([root])
        while node_queue:
            level_size = len(node_queue)
            for i in range(level_size):
                node = node_queue.popleft()
                if i == level_size - 1:  # if this is the last node in this level
                    res.append(node.val)

                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
        return res
