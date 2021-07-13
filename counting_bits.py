class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        answer = [0]
        for i in range(1, n + 1):
            answer.append(answer[i >> 1] + i % 2)
        return answer
