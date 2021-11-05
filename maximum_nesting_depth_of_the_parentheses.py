class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth: int = 0
        opened: int = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                opened += 1
                max_depth = max(max_depth, opened)
            if s[i] == ')':
                opened -= 1
        
        return max_depth
