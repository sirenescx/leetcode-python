class Solution:
    def robbery(self, nums: List[int], start: int, end: int) -> int:
        houses: List[int] = [0] * (end - start)
        houses[0] = nums[start] 
        houses[1] = nums[start + 1] 
        houses[2] = max(nums[start] + nums[start + 2], nums[start + 1]) 
        
        for i in range(start + 3, end):
            houses[i - start] = nums[i] + max(houses[i - start - 2], houses[i - start - 3])
        
        return max(houses[-1], houses[-2])
        
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(max(nums[0], nums[1]), nums[2])
        
        n: int = len(nums)

        return max(self.robbery(nums, 0, n - 1), self.robbery(nums, 1, n))
             
