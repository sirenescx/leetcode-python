class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        step_sum: int = 0
        negative_sum: int = 0
            
        for i in range(len(nums)):
            step_sum += nums[i]
            negative_sum = min(negative_sum, step_sum)
        
        return -negative_sum + 1
