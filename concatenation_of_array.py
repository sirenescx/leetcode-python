class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length: int = len(nums)
        concatenation: List[int] = [0] * 2 * length
        for i in range(length):
            concatenation[i] = concatenation[length + i] = nums[i]
        
        return concatenation
        
