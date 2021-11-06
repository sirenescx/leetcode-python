class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_max: int = max(nums[0], nums[1])
        second_max: int = min(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            if nums[i] > first_max:
                second_max = first_max
                first_max = nums[i]
            elif nums[i] > second_max:
                second_max = nums[i]
        
        return (first_max - 1) * (second_max - 1)
