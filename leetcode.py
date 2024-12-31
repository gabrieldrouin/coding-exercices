from collections import deque
from typing import Optional

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next: ListNode = None

def buildList(values, pos):
    if not values:
        return None
    
    # Create nodes
    nodes = [ListNode(val) for val in values]
    
    # Link nodes
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Create cycle if pos is valid
    if pos >= 0 and pos < len(nodes):
        nodes[-1].next = nodes[pos]
    
    return nodes[0]
        
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        curr = head
        prev = curr

        while True:
            curr = curr.next
            if not curr:
                return False
            if curr.val == "x":
                return True
            prev.val = "x"
            prev = curr

        

sol = Solution()
head1 = buildList([3,2,0,-4], 1)
head2 = buildList([1, 2], 0)
head3 = buildList([1], -1)
print(sol.hasCycle(head1))
print(sol.hasCycle(head2))
print(sol.hasCycle(head3))