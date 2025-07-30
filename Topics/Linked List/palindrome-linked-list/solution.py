# https://leetcode.com/problems/palindrome-linked-list

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: Optional[ListNode]) -> bool:
    stack = []
    dummy = head
    while dummy:
        stack.append(dummy.val)
        dummy = dummy.next

    dummy = head
    while dummy and dummy.val == stack.pop():
        dummy = dummy.next

    return True if dummy is None else False
    
# Test Case:

head = [1,2,2,1]
output = True

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

print(isPalindrome(list_to_linkedlist(head)) == output)