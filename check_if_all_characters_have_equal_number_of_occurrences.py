class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occurrences = {}
        for c in s:
            if c in occurrences:
                occurrences[c] += 1
            else:
                occurrences[c] = 1
        
        count = occurrences[s[0]]
        for letter in occurrences:
            if occurrences[letter] != count:
                return False
        
        return True

        # return len(set(Counter(s).values())) == 1
