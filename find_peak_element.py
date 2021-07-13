class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         if len(nums) > 1:
#             prev = float('-inf')
#             nums.append(prev)
#             cur = nums[0]
#             next = nums[1]
#             nums.append(nums[-1] - 1)
#             for i in range(len(nums) - 1):
#                 if cur > prev and cur > next:
#                     return i
#                 prev = cur
#                 cur = nums[i + 1]
#                 next = nums[i + 2] 
        
#         return 0
    
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
            
        return left
            
