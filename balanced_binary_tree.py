# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    balanced: bool = True
    
    def depth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        left_depth: int = self.depth(root.left)
        right_depth: int = self.depth(root.right)
        
        if (abs(left_depth - right_depth)) > 1:
            self.balanced = False
            
        return max(left_depth, right_depth) + 1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        self.depth(root)
        
        return self.balanced
