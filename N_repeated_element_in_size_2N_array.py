class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # return (sum(nums) - sum(set(nums))) // (len(nums) // 2 - 1)
        
        
#         repeats: set = set()
#         for num in nums:
#             if num in repeats:
#                 return num
#             repeats.add(num)
        
#         raise Exception()
    
        
        n: int = len(nums)
            
        for i in range(1, 4):
            for j in range(0, n - i):
                if nums[j] == nums[j + i]:
                    return nums[j]
        
        raise Exception()
