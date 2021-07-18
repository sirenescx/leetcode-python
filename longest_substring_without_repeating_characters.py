class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = {}
        start_index = 0
        end_index = -1
        longest = 0
        for i in range(len(s)):
            if not s[i] in track:
                track[s[i]] = i
            else:
                longest = max(longest, end_index - start_index + 1)
                start_index = max(start_index, track[s[i]] + 1)    
                track[s[i]] = i
            end_index = i
            
        return max(longest, end_index - start_index + 1)
        
