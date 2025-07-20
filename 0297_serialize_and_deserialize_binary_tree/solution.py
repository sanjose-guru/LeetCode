# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        vals = []

        def dfs_preorder(node: TreeNode):
            if not node:
                vals.append("#")
                return

            vals.append(str(node.val))  # inorder process current node only
            dfs_preorder(node.left)
            dfs_preorder(node.right)

        dfs_preorder(root)
        return " ".join(vals)  # space will help seperate multi digit nums

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split())

        def dfs_preorder():
            val = next(vals)

            if val == "#":
                return None

            node = TreeNode(int(val))  # in preordr we process current node only
            node.left = dfs_preorder()  # walk down left
            node.right = dfs_preorder()  # walk one right
            return node

        return dfs_preorder()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
