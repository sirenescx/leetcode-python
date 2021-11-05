class Solution:
    def maxProduct(self, nums: List[int]) -> int:
#         dp: List[[int]] = [[0] * 2 for i in range(len(nums))]
#         dp[0][0] = dp[0][1] = nums[0]
#         max_subproduct = nums[0]
#         for i in range(1, len(nums)):
#             dp[i][0] = max(max(nums[i], nums[i] * dp[i - 1][0]), nums[i] * dp[i - 1][1]) 
#             dp[i][1] = min(min(nums[i], nums[i] * dp[i - 1][0]), nums[i] * dp[i - 1][1])
#             if max(dp[i][0], dp[i][1]) > max_subproduct:
#                 max_subproduct = max(dp[i][0], dp[i][1])
        
#         return max_subproduct
        
        max_product: int = nums[0]
        maximum: int = max_product
        minimum: int = max_product
            
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maximum, minimum = minimum, maximum
                
            maximum = max(nums[i], maximum * nums[i])
            minimum = min(nums[i], minimum * nums[i])
            max_product = max(max_product, maximum)
        
        return max_product
            
            
