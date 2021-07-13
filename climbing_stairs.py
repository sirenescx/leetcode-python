class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n + 1):
            next = first + second
            first = second
            second = next
        
        return second
