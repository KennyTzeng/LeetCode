"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        return self.getMaxDepth(root)

    def getMaxDepth(self, node):
        if node != None:
            if len(node.children) != 0:
                return max(self.getMaxDepth(child) for child in node.children) + 1
            else:
                return 1
        else:
            return 0

# testing
# root = Node(1, [Node(3, [Node(5,[]), Node(6,[])]), Node(2,[]), Node(4,[])])
# print(Solution().maxDepth(root))