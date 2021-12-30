class Solution:
    def reverseNumber(self, num: int) -> int:
        new_num: int = 0
        while num > 0:
            new_num = new_num * 10 + num % 10
            num //= 10
        
        return new_num
    
    def isSameAfterReversals(self, num: int) -> bool:
        return self.reverseNumber(self.reverseNumber(num)) == num
