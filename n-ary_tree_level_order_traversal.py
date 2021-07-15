"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def dfs(self, root, result, level):
        if root == None:
            return
        if len(result) <= level:
            result.append([])
        result[level].append(root.val)
        if root.children == None:
            return
        for child in root.children:
            self.dfs(child, result, level + 1)
        level += 1
    
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(root, result, 0)
        
        return result
