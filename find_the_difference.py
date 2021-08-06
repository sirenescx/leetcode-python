class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_letters = {}
        t_letters = {}
        for c in s:
            if c in s_letters:
                s_letters[c] += 1
            else:
                s_letters[c] = 1
                
        for c in t:
            if c in t_letters:
                t_letters[c] += 1
            else:
                t_letters[c] = 1  
        
        for key in t_letters:
            if key in s_letters:
                t_letters[key] -= s_letters[key]
            else:
                return key
        
        for key, val in t_letters.items():
            if val != 0:
                return key
        
        return ""
        
