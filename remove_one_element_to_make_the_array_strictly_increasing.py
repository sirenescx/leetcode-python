class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        stack = []
        for i in range(1, len(nums)): 
            if nums[i - 1] >= nums[i]: 
                stack.append(i)
                
        if len(stack) == 0: 
            return True 
        if len(stack) > 1: 
            return False
        
        index = stack[0]
        return (index == 1 or nums[index - 2] < nums[index]) or (index == len(nums) - 1 or nums[index - 1] < nums[index + 1])
