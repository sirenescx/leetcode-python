class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_subsum: int = nums[0]
        min_subsum: int = nums[0]
        current_max: int = 0
        current_min: int = 0
        total_sum: int = 0
            
        for i in range(len(nums)):
            current_max = max(current_max + nums[i], nums[i])
            max_subsum = max(max_subsum, current_max)
            current_min = min(current_min + nums[i], nums[i])
            min_subsum = min(min_subsum, current_min)
            total_sum += nums[i]
            
        return max(max_subsum, total_sum - min_subsum) if max_subsum > 0 else max_subsum
                   
#         subsums = [0] * n
#         subsums[0] = nums[0]
#         for i in range(1, n):
#             subsums[i] = max(nums[i], nums[i] + subsums[i - 1])
#             max_subsum = max(max_subsum, subsums[i])    
            
#         for c in range(max(0, n // 2 - 50), min(n // 2 + 50 + 1, n)):   
#             new_nums = nums[c:] + nums[:c]

#             subsums = [0] * n
#             subsums[0] = new_nums[0]
#             for i in range(1, n):
#                 subsums[i] = max(new_nums[i], new_nums[i] + subsums[i - 1])
#                 max_subsum = max(max_subsum, subsums[i])   
                
#         return max_subsum
    
        
        
