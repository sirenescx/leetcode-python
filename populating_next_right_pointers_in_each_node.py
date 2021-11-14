"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def dfs(self, left: 'Node', right: 'Node'):
        if left and right:
            left.next = right

            self.dfs(left.left, left.right)
            self.dfs(right.left, right.right)
            self.dfs(left.right, right.left)
            
    def connect(self, root: 'Node') -> 'Node':
        if root != None:
            root.next = None
            self.dfs(root.left, root.right)
        
        return root
