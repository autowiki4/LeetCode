"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        o_to_n = {}
        start = node
        stack = [start]
        visited = set()
        visited.add(start)

        while stack:
            curr = stack.pop()
            o_to_n[curr] = Node(val = curr.val)
            for nei in curr.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)
        
        for old, new in o_to_n.items():
            for nei in old.neighbors:
                curr = o_to_n[nei]
                new.neighbors.append(curr)
        
        return o_to_n[node]