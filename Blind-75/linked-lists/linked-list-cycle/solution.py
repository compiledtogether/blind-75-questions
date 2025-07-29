# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: Optional[ListNode]) -> bool:
    fast = slow = head

    while fast and fast.next:
        slow = slow.next # type: ignore
        fast = fast.next.next

        if fast == slow:
            return True # Cycle detected
    
    return False # No cycle

# Test case:

head = [3,2,0,-4]
output = True