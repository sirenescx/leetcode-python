class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        subsums = [0] * len(nums)
        subsums[0] = nums[0]
        max_subsum = nums[0]
        for i in range(1, len(nums)):
            subsums[i] = max(nums[i], nums[i] + subsums[i - 1])
            if subsums[i] > max_subsum:
                max_subsum = subsums[i]
        
        return max_subsum
            
