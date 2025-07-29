# https://leetcode.com/problems/middle-of-the-linked-list
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    first = second = head

    while second and second.next:
        first = first.next # type: ignore
        second = second.next.next

    return first

# Test Case:

head = [1,2,3,4,5]
output = [3,4,5]

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

print(linkedlist_to_list(middleNode(list_to_linkedlist(head))) == output)