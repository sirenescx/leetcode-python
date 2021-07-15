# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, root, x, level, result):   
        if root == None:
            return
        if (root.left != None and root.left.val == x) or (root.right != None and root.right.val == x):
            result.append(level + 1)
            result.append(root.val)
            
        self.dfs(root.left, x, level + 1, result)
        self.dfs(root.right, x, level + 1, result)
   
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        x_result = []
        y_result = []
        self.dfs(root, x, 0, x_result)
        self.dfs(root, y, 0, y_result)
        
        return len(x_result) != 0 and len(y_result) != 0 and x_result[0] == y_result[0] and x_result[1] != y_result[1]
        
