class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum: List[int] = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            running_sum[i] = nums[i] + running_sum[i - 1]
        
        return running_sum
