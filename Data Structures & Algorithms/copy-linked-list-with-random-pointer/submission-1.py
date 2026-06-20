"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {None: None}

        cur = head
        while cur:
            mp[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            mp[cur].next = mp[cur.next]
            mp[cur].random = mp[cur.random]
            cur = cur.next
        
        return mp[head]