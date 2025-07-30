# https://leetcode.com/problems/reverse-linked-list
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    prev = None
    while curr:
        temp = curr.next # store the next node
        curr.next = prev # reverse the pointer
        prev = curr # move prev forward
        curr = temp # move prev forward

    return prev # prev is the new head of the reversed list

# Test Case:

head = [1,2,3,4,5]
output = [5,4,3,2,1]

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

print(linkedlist_to_list(reverseList(list_to_linkedlist(head))) == output)




        