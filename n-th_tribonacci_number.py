class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        numbers = [0] * (n + 1)
        numbers[0] = 0
        numbers[1] = 1
        numbers[2] = 1
        for i in range(3, n + 1):
            numbers[i] = numbers[i - 1] + numbers[i - 2] + numbers[i - 3]
        
        return numbers[n]
