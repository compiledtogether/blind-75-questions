# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    resultHead = result
    while list1 and list2:
        if list1.val > list2.val:
            result.next = list2
            list2 = list2.next
        else:
            result.next = list1
            list1 = list1.next

        result = result.next

    result.next = list1 if list1 else list2

    return resultHead.next

# Test Case:

list1 = [1,2,4]
list2 = [1,3,4]
output = [1,1,2,3,4,4]

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

list1_array = list_to_linkedlist(list1)
list2_array = list_to_linkedlist(list2)

print(linkedlist_to_list(mergeTwoLists(list1_array, list2_array)) == output)