# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        count, index = 1, size - n + 1
        curr, prev = head, None
        while count < index:
            count += 1
            prev = curr
            curr = curr.next
        tmp = curr.next
        if not prev:
            curr.next = None
            return tmp
        elif curr.next:
            prev.next = tmp
            curr.next = None
        else:
            prev.next = None
        return head
        