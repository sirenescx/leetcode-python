# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, root, average, counts, level):
        if root == None:
            return 
        if len(average) <= level:
            average.append(root.val)
            counts.append(1)
        else:
            average[level] += root.val
            counts[level] += 1
        
        self.dfs(root.left, average, counts, level + 1)
        self.dfs(root.right, average, counts, level + 1)
        
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        average = []
        counts = []
        
        self.dfs(root, average, counts, 0)
        for i in range(len(average)):
            average[i] = float(average[i]) / counts[i]
        
        return average
