class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0
        right = num
        while left <= right:
            mid = (left + right) / 2
            if mid ** 2 == num:
                return True
            if mid ** 2 <= num:
                left = int(mid) + 1
            else:
                right = int(mid) - 1
            
        return False
