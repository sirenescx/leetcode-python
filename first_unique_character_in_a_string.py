class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts: map = {}
        positions: map = {}
            
        for i in range(len(s)):
            char: str = s[i]
            if char not in counts:
                counts[char] = 1
                positions[char] = i
            else:
                counts[char] += 1
                
        min_pos: int = len(s)
        for char, count in counts.items():
            if count == 1:
                if positions[char] < min_pos:
                    min_pos = positions[char]
        
        return -1 if min_pos == len(s) else min_pos
            
