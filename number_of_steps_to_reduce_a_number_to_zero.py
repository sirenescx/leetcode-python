class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps: int = 0
        while num != 0:
            if (num & 1) == 0:
                num >>= 1
            else:
                num -= 1
            steps += 1
        
        return steps
