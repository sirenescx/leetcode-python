class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum: int = 0
        suffix_sum: int = sum(nums)
            
        for i in range(len(nums)):
            suffix_sum -= nums[i]
            if suffix_sum == prefix_sum:
                return i
            prefix_sum += nums[i]
            
        return -1
    
#         prefix_sum: List[int] = [0] * (len(nums) + 2)
#         prefix_sum[1] = nums[0]
        
#         for i in range(1, len(nums)):
#             prefix_sum[i + 1] = prefix_sum[i] + nums[i]
         
#         for i in range(1, len(prefix_sum) - 1):
#             if prefix_sum[i - 1] == prefix_sum[-2] - prefix_sum[i]:
#                 return i - 1
        
#         return -1
