class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        score: int = 0
        max_index: int = 0
        
        for i in range(1, len(values)):
            score = max(score, max(values[i - 1] + values[i] - 1, values[max_index] + values[i] + max_index - i))
            if values[i] + i >= values[max_index] + max_index:
                max_index = i
        
        return score
            
