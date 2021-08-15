class Solution:
    def makeFancyString(self, s: str) -> str:
        prev = s[0]
        new_s = prev
        count = 1
        for i in range(1, len(s)):
            if s[i] == prev:
                if count < 2:
                    new_s += s[i]
                count += 1
            else:
                new_s += s[i]
                prev = s[i]
                count = 1
        
        return new_s 
            
