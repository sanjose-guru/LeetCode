# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        # Root node in inorder array splits/partitions the left subtree and right subtree
        # to speed up root node index lookup we will create this hashmap
        root_lookup = {val: idx for idx, val in enumerate(inorder)}

        def helper(preorder_lb, preorder_rb, inorder_lb, inorder_rb):
            if preorder_lb > preorder_rb or inorder_lb > inorder_rb:
                return None

            # first element in preorder is always root
            r_val = preorder[preorder_lb]
            r = TreeNode(r_val)

            # get root index from inorder (this is going to split inorder into left and right subtrees)
            r_idx = root_lookup[r_val]

            # lift subtree is in the left partion on the inorder array, so get the size
            l_tree_size = r_idx - inorder_lb

            # left subtree
            r.left = helper(
                preorder_lb + 1, preorder_lb + l_tree_size, inorder_lb, r_idx - 1
            )
            r.right = helper(
                preorder_lb + 1 + l_tree_size, preorder_rb, r_idx + 1, inorder_rb
            )
            return r

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)

    def buildTree_verbose(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:

        # base case, if the list is empty we have nothing to construct.
        if not preorder or not inorder:
            return None

        # 1st node in preorder is the root
        root_val = preorder[0]

        # look up this root in inorder array and find the left partition and right partition
        root_idx = inorder.index(preorder[0])
        l_inorder = inorder[:root_idx]
        r_inorder = inorder[root_idx + 1 :]

        l_tree_size = len(l_inorder)
        l_preorder = preorder[1 : l_tree_size + 1]
        r_preorder = preorder[l_tree_size + 1 :]

        root = TreeNode(root_val)
        root.left = self.buildTree(l_preorder, l_inorder)
        root.right = self.buildTree(r_preorder, r_inorder)

        return root
