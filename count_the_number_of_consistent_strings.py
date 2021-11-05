class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set: set = set(list(allowed))
        consistent: int = 0
        
        for word in words:
            for char in word:
                if char not in allowed_set:
                    break
            else:
                consistent += 1
        
        return consistent
