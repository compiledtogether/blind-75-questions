# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    fast = slow = head

    while fast and fast.next:
        slow = slow.next # type: ignore
        fast = fast.next.next

        if fast == slow:
            break # Cycle detected
    
    else: return None # No cycle

    fast = head

    while fast != slow:
        fast = fast.next # type: ignore
        slow = slow.next # type: ignore
    
    return slow

# Test case:

head = [3,2,0,-4]
pos = 1
Output = "tail connects to node index 1"
