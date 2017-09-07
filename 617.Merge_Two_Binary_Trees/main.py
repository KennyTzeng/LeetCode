# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if(t1):
            t1.val += t2.val if t2 else 0
        else:
            t1 = TreeNode(t2.val) if t2 else None

        if(t1):
            t1.left = self.mergeTrees(t1.left, t2.left) if t2 else t1.left
            t1.right = self.mergeTrees(t1.right, t2.right) if t2 else t1.right

        return t1    