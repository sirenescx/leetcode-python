class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels: set =  ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        n: int = len(s)
        left: int = 0
        right: int = 0
        
        for i in range(n // 2):
            left += s[i] in vowels
            right += s[n - i - 1] in vowels
        
        return left == right
