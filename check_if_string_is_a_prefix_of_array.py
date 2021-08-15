class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:        
        if s == words[0]:
            return True
        
        if s[0] != words[0][0] or len(s) < len(words[0]):
            return False
        
        s = s[len(words[0]):]
            
        for i in range(1, len(words)):
            if s[0] != words[i][0] or len(s) < len(words[i]):
                return False
            if s == words[i]:
                return True
            s = s[len(words[i]):]
        
        return False
