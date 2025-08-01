
from typing import Optional, List
from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

def maxDepth(root: 'Node') -> int:
    if not root:
        return 0
    max_depth = 0
    for child in root.children: # type: ignore
        max_depth = max(max_depth, maxDepth(child))
    return max_depth + 1
        
# Test Case:

root = [1,None,3,2,4,None,5,6]
output = 3