class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numbers: List[int] = [0] * (100 + 2)
        for num in nums:
            numbers[num + 1] += 1
        for i in range(1, len(numbers)):
            numbers[i] += numbers[i - 1]
        
        return [numbers[num] for num in nums] 
        

                
            
        
