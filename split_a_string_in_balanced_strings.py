class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced: int = 0
        left: int = 0
        right: int = 0
        
        for i in range(len(s)):
            if s[i] == 'R':
                right += 1
            elif s[i] == 'L':
                left += 1
            if left == right:
                balanced += 1
                right = 0
                left = 0
        
        return balanced
