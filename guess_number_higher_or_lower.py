# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left <= right:
            mid = (right + left) // 2
            guess_ans = guess(mid)
            if guess_ans == 0:
                return mid
            if guess_ans < 0:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
        
