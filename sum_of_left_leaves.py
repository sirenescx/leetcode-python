# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sumOfLeaves: int = 0
        
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int: 
        if root == None:
            return self.sumOfLeaves
        
        if root.left != None and root.left.left == None and root.left.right == None:
            self.sumOfLeaves += root.left.val
            
        self.sumOfLeftLeaves(root.left)
        self.sumOfLeftLeaves(root.right)
        
        return self.sumOfLeaves
