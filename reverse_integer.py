class Solution(object):
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversed_num = 0
        
        sgn = -1 if x < 0 else 1
        bound = 2**31 - 1
        x = abs(x)
        while x != 0:
          digit = x % 10
          x //= 10
          if (bound / 10 - abs(reversed_num) < abs(digit) - 1):
            return 0
          reversed_num *= 10 
          reversed_num += digit

        return reversed_num * sgn

            
        
        
