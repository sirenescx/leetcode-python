# Approach
Reverse number using modulo division

# Code
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        left: int = x
        right: int = 0

        while x > 0:
            right = right * 10 + x % 10
            x //= 10
        
        return left == right
```
