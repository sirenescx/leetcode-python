class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        divisors_sum: int = 1
        i: int = 2
        while i * i <= num:
            if num % i == 0:
                divisors_sum += i
                if i * i != num:
                    divisors_sum += num // i
            i += 1
        
        return divisors_sum == num
