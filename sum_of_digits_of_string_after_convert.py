class Solution:
    def getLucky(self, s: str, k: int) -> int:
        n = 0
        for c in s:
            num = ord(c) - 96
            if num // 10 > 0:
                n = n * 100 + num
            else:
                n = n * 10 + num
        
        temp = 0 
        while k > 0:
            while n > 0:
                temp += n % 10
                n //= 10
            
            n = temp
            temp = 0
            k -= 1
        
        return n
