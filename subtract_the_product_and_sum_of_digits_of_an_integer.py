class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_of_digits: int = 0
        product_of_digits: int = 1
        
        while n > 0:
            sum_of_digits += n % 10
            product_of_digits *= n % 10
            n //= 10
        
        return product_of_digits - sum_of_digits
