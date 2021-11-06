class Solution:
    def sumBase(self, n: int, k: int) -> int:
        sum_base_k: int = 0
            
        while n > 0:
            sum_base_k += n % k
            n //= k
        
        return sum_base_k
