class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size: int = len(s1)
        s1_map: Counter = Counter(s1)
        s2_sub_map: Counter = Counter(s2[:window_size])
        
        if s1_map == s2_sub_map:
            return True
        
        for i in range(1, len(s2) - window_size + 1):
            if s2_sub_map[s2[i - 1]] == 1:
                del s2_sub_map[s2[i - 1]]
            else:
                s2_sub_map[s2[i - 1]] -= 1
            s2_sub_map[s2[window_size + i - 1]] += 1
            if s1_map == s2_sub_map:
                return True     
        
        return False
