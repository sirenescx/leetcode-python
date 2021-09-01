# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def traversal(self, left_root: Optional[TreeNode], right_root: Optional[TreeNode]):
        if left_root is None or right_root is None:
            return left_root == right_root
        
        if left_root.val == right_root.val:
            return self.traversal(left_root.left, right_root.right) and self.traversal(left_root.right, right_root.left)

        return False
        
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.traversal(root.left, root.right)
