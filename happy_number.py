class Solution:
    def isHappy(self, n: int) -> bool:
        number: int = 0
         
        prev = n
        while n > 4 and n != 1:
            while n > 0:
                number += (n % 10)**2
                n //= 10
            n = number
            number = 0
        
        return n % 10 == 1
