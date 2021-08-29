class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        lower: int = nums[-1]
        high: int = len(nums) - 1
        
        for i in range(high - k + 1, -1, -1):
            lower = min(nums[high] - nums[i], lower)
            high -= 1
        
        return lower
