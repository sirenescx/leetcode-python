# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    range_sum: int = 0
        
    def dfs(self, root: Optional[TreeNode], low: int, high: int):
        if root == None:
            return
            
        if low < root.val:
            self.dfs(root.left, low, high)
        if low <= root.val <= high:
            self.range_sum += root.val      
        if root.val < high:
            self.dfs(root.right, low, high)

        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.dfs(root, low, high)
        return self.range_sum
