class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count: List[int] = [0] * (max(nums) + 1)
            
        for num in nums:
            count[num] += num
            
        previous: int = 0
        current: int = 0

        for i in range(0, len(count)):
            previous, current = current, max(previous + count[i], current)
        
        return current
