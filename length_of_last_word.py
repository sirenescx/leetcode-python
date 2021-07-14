class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        for i in range(len(s)):
            if s[len(s) - i - 1] != ' ':
                length += 1
            else:
                if length != 0:
                    break
        
        return length
