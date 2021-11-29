class Solution:
    def numTeams(self, rating: List[int]) -> int:
        lower_left: List[int] = [0] * len(rating)
        greater_left: List[int] = [0] * len(rating)
        lower_right: List[int] = [0] * len(rating)
        greater_right: List[int] = [0] * len(rating)
        
        for i in range(len(rating)):
            for j in range(i):
                if rating[j] > rating[i]:
                    greater_left[i] += 1
                if rating[j] < rating[i]:
                    lower_left[i] += 1
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    greater_right[i] += 1
                if rating[j] < rating[i]:
                    lower_right[i] += 1                   
        
        answer: int = 0
        for i in range(len(lower_left)):
            answer += lower_left[i] * greater_right[i]
            answer += greater_left[i] * lower_right[i]
            
        return answer
            
