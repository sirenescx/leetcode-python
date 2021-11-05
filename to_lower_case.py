class Solution:
    def toLowerCase(self, s: str) -> str:
        a_upper: int = ord('A')
        a_lower: int = ord('a')
        chars: List[str] = [''] * len(s)
        for i, c in enumerate(s):
            if 'A' <= c <= 'Z':
                chars[i] = chr(a_lower + ord(c) - a_upper)
            else:
                chars[i] = c
        
        return ''.join(chars)
                
