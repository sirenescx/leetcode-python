class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        degrees = {}
        left = {}
        right = {}
        for i in range(len(nums)):
            if nums[i] not in left:
                left[nums[i]] = i
            right[nums[i]] = i
            if not nums[i] in degrees:
                degrees[nums[i]] = 1
            else:
                degrees[nums[i]] += 1
        
        result = len(nums)
        max_degree = max(degrees.values())
        for i in degrees:
            if degrees[i] == max_degree:
                result = min(result, right[i] - left[i] + 1)
               
        return result
            
