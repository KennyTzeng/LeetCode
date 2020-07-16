# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
            
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        walk = head
        
        while l1 and l2:
            if l1.val <= l2.val:
                walk.next = l1
                l1 = l1.next
            else:
                walk.next = l2
                l2 = l2.next
            walk = walk.next
                
        if l1:
            walk.next = l1
        else:
            walk.next = l2
            
        return head