class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        n_1 = 1
        n_2 = 0
        for i in range(2, n + 1):
            cur = n_1 + n_2
            n_2 = n_1
            n_1 = cur
        
        return n_1
