# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # call-by-object
        check(root, None, None)
        return root

def check(node, parent, direction):
    # check left subtree
    if node.left != None:
        check(node.left, node, "left")
    
    # check right subtree
    if node.right != None:
        # optimization
        if check(node.right, node, "right"):
            return True

    # delete node if val = 0 and is leaf
    if node.val == 0 and node.left == None and node.right == None:
        if direction == "left":
            parent.left = None
        elif direction == "right":
            parent.right = None
        return False
    return True

