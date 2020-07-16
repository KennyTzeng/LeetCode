# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        node = root
        
        if node == None:
            return TreeNode(val)
        else:
            while node != None:
                if val > node.val:
                    if node.right != None:
                        node = node.right
                    else:
                        node.right = TreeNode(val)
                        break
                else:
                    if node.left != None:
                        node = node.left
                    else:
                        node.left = TreeNode(val)
                        break

        return root