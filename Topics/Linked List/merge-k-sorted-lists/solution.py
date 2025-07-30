# https://leetcode.com/problems/merge-k-sorted-lists

from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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
    
    def divideAndConquer(lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return lists[left]
        
        mid = (left + right) // 2
        l1 = divideAndConquer(lists, left, mid)
        l2 = divideAndConquer(lists, mid + 1, right)

        return mergeTwoLists(l1, l2)
    
    if not lists:
        return None
    return divideAndConquer(lists, 0, len(lists) - 1)

# Test Case:

lists = [[1,4,5],[1,3,4],[2,6]]
output = [1,1,2,3,4,4,5,6]

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

input = []
for list in lists:
    input.append(list_to_linkedlist(list))    

print(linkedlist_to_list(mergeKLists(input)) == output)