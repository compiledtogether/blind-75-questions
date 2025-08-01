# https://leetcode.com/problems/serialize-and-deserialize-bst

from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return "N"
        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def build(vals):
            val = next(vals)
            if val == "N": return None
            node = TreeNode(int(val))
            node.left = build(vals) # type: ignore
            node.right = build(vals) # type: ignore
            return node
        return build(iter(data.split(",")))
        

# Test Case:

root = [1,2,3,None,None,4,5]
output = [1,2,3,None,None,4,5]