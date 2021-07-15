# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValid(self, root, left, right):
        if root == None:
            return True
        if left < root.val < right:
            return self.isValid(root.left, left, root.val) and self.isValid(root.right, root.val, right)
   
        return False
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root, float('-inf'), float('inf'))
        
        
        
