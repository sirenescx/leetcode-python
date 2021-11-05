class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        
        houses: List[int] = [0] * len(nums)
        houses[0] = nums[0]
        houses[1] = nums[1]
        houses[2] = max(nums[0] + nums[2], nums[1])
        
        for i in range(3, len(nums)):
            houses[i] = nums[i] + max(houses[i - 2], houses[i - 3])
        
        return max(houses[-1], houses[-2])
