class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        prefix_min: int = nums[0]
        max_difference: int = -1
            
        for i in range(1, len(nums)):
            if prefix_min < nums[i]:
                max_difference = max(max_difference, nums[i] - prefix_min)
            else:
                prefix_min = nums[i]
        
        return max_difference
