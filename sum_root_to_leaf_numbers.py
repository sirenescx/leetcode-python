# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum_numbers: int = 0
    
    def dfs(self, root: Optional[TreeNode], value: int):
        if root == None:
            return
        
        if root.left == None and root.right == None:
            self.sum_numbers += value
            return
        
        value = value * 10
        if root.left != None:
            self.dfs(root.left, value + root.left.val)
        if root.right != None:
            self.dfs(root.right, value + root.right.val)
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, root.val)
        return self.sum_numbers
