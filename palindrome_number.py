class Solution(object):
    def length(self, x):
        return int(ceil(log10(abs(x) + 0.5)))
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        if x < 10:
            return True
        left = 0
        while (self.length(x) - self.length(left) > 1):
            left *= 10
            left += x % 10
            x //= 10
        
        return True if left == x or (left == x // 10 and left != 0) else False
