# https://leetcode.com/problems/reverse-nodes-in-k-group
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    ## Recursive Approach

    ## Check if we need to reverse the group
    # curr = head
    # for _ in range(k):
    #     if not curr: return head
    #     curr = curr.next
            
            
    # # Reverse the group (basic way to reverse linked list)
    # prev = None
    # curr = head
    # for _ in range(k):
    #     nxt = curr.next # type: ignore
    #     curr.next = prev # type: ignore
    #     prev = curr
    #     curr = nxt
    
    
    # # After reverse, we know that `head` is the tail of the group.
    # # And `curr` is the next pointer in original linked list order
    # head.next = reverseKGroup(curr, k) # type: ignore
    # return prev

    ## Iterative Approach
    if not head or k == 1:
        return head

    dummy = ListNode()
    dummy.next = head
    prev = dummy
    curr = head

    # Count the number of nodes in the list
    count = 0
    while curr:
        count += 1
        curr = curr.next

    # Reverse k nodes at a time
    while count >= k:
        curr = prev.next # type: ignore
        nxt = curr.next # type: ignore

        # Reverse k nodes
        for _ in range(1, k):
            curr.next = nxt.next # type: ignore
            nxt.next = prev.next # type: ignore
            prev.next = nxt # type: ignore
            nxt = curr.next # type: ignore

        prev = curr
        count -= k

    return dummy.next

# Test Case:

head = [1,2,3,4,5]
k = 2
output = [2,1,4,3,5]

# Helper to convert a list to a linked list
def list_to_linkedlist(list):
    dummy = ListNode()
    current = dummy
    for val in list:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper to convert a linked list back to a list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

print(linkedlist_to_list(reverseKGroup(list_to_linkedlist(head), k)) == output)
        