class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn_counter: Counter = Counter(ransomNote)
        m_counter: Counter = Counter(magazine)
        for key in rn_counter:
            if not key in m_counter or rn_counter[key] > m_counter[key]:
                return False
        
        return True
