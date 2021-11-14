class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: List[int] = []
        stack.append(0)
        answer: List[int] = [0] * len(temperatures)
        
        for i in range(1, len(temperatures)):
            while not len(stack) == 0 and temperatures[i] > temperatures[stack[-1]]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
            
        return answer
                
            
