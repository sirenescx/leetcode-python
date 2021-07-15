# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, root, traversal, level):
        if root == None:
            return
        if len(traversal) <= level:
            traversal.append([])
        traversal[level].append(root.val)
        
        self.dfs(root.left, traversal, level + 1)
        self.dfs(root.right, traversal, level + 1)
        
        level += 1
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        traversal = []
        self.dfs(root, traversal, 0)
        
        return traversal
