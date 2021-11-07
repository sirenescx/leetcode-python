class Solution:
    def jump(self, nums: List[int]) -> int:
        dp: List[int] = [inf] * len(nums)
        dp[0] = 0
        current: int = 0
        
        for i in range(0, len(nums)):
            for j in range(current + 1, min(i + nums[i] + 1, len(nums))):
                dp[j] = min(dp[j], dp[i] + 1)
            current = max(current, i + nums[i])
               
        return dp[-1]
