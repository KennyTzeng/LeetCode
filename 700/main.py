# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        node = root
        while node:
            if val == node.val:
                return node
            elif val > node.val:
                if node.right:
                    node = node.right
                else:
                    return None
            elif val < node.val:
                if node.left:
                    node = node.left
                else:
                    return None
        return None