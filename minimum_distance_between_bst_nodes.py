# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    result = float('inf')
    previous = float('-inf')
    
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left != None:
            self.minDiffInBST(root.left)
        self.result = min(self.result, root.val - self.previous)
        self.previous = root.val
        if root.right != None:
            self.minDiffInBST(root.right)     
            
        return self.result
