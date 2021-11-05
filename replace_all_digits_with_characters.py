class Solution:
    def replaceDigits(self, s: str) -> str:
        letters: List[str] = [''] * len(s)
            
        for i in range(len(s)):
            letters[i] = chr(ord(s[i - 1]) + int(s[i])) if s[i].isdigit() else s[i]
        
        return ''.join(letters)
                
