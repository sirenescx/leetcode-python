class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        nums = [0] * (n + 1)
        nums[0] = 0
        nums[1] = 1
        max_num = 0
        for i in range(2, n + 1):
            nums[i] = nums[i >> 1] if i % 2 == 0 else nums[i >> 1] + nums[(i >> 1) + 1]
            if nums[i] > max_num:
                max_num = nums[i]
  
        return max_num
