# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev, curr = None, head
        while curr.next is not None:
            if prev is None:
                l = ListNode(curr.val)
            else:
                l = ListNode(curr.val, prev)
            prev = l
            curr = curr.next
        h = ListNode(curr.val, prev)
        return h
            
            