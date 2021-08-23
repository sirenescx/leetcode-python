class Solution:
    def gcd(self, a: int, b: int) -> int:
        while a:
            a, b = b % a, a
            
        return b
     
    def findGCD(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum: int = nums[0]
        maximum: int = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            if num > maximum:
                maximum = num
                continue
            if num < minimum:
                minimum = num
        
        return gcd(maximum, minimum)
  
