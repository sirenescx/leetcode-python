class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        max_distance: int = nums[0]
        if max_distance == 0:
            return False
        
        for i in range(1, len(nums) - 1):
            if nums[i] == 0 and max_distance == i:
                return False
            max_distance = max(max_distance, nums[i] + i)
        
        return max_distance >= len(nums) - 1
