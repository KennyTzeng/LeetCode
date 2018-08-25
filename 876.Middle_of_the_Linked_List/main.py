# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        index = 0
        node = head
        while node.next != None:
            node = node.next
            index += 1
        mid = int((index+1)/2)

        node = head
        for i in range(mid):
            node = node.next

        return node
