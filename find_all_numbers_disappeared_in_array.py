class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         result: set = set(range(1, len(nums) + 1))
#         for num in nums:
#             if num in result:
#                 result.discard(num)
        
#         return list(result)        
        for i in range(len(nums)):
            nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
            
        result: List[int] = list()
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        
        return result
