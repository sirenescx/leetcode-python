class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        maximum: int = max(nums[0], nums[1])
        second_maximum: int = min(nums[0], nums[1])
        minimum: int = min(nums[0], nums[1])
        second_minimum: int = max(nums[0], nums[1])   
            
        for i in range(2, len(nums)):
            num = nums[i]
            if num > maximum:
                second_maximum = maximum
                maximum = num
            elif num > second_maximum:
                second_maximum = num
                
            if num < minimum:
                second_minimum = minimum
                minimum = num
            elif num < second_minimum:
                second_minimum = num
        
        return (maximum * second_maximum) - (minimum * second_minimum)
            
            
        
        
