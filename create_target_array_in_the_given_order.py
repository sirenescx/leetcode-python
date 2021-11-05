class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        output: List[int] = []
        for i in range(len(nums)):
            output.insert(index[i], nums[i])
        
        return output
        
