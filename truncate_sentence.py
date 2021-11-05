class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        index: int = 0
            
        for c in s:
            index += 1
            if c == ' ':
                k -= 1
                if k == 0:
                    index -= 1
                    break
        
        return s[:index]
                    
