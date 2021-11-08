class Solution:
    def factorial(self, n: int) -> int:
        fact: int = 1
        for i in range(2, n + 1):
            fact *= i
        
        return fact
        
    def numTrees(self, n: int) -> int:
        return self.factorial(2 * n) // self.factorial(n + 1) // self.factorial(n)
