class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
#         if x == 0:
#             return 0
        
#         num = 3
#         sqrt = 0
#         while x > 0:
#             x -= num
#             num += 2
#             sqrt += 1
        
#         return sqrt - 1 if num < 0 else sqrt

        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 <= x:
                left = mid + 1
            else:
                right = mid - 1
        
        return left - 1
