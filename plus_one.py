class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)):
            if digits[len(digits) - i - 1] + 1 > 9:
                digits[len(digits) - i - 1] = 0
                if len(digits) - i - 1 == 0:
                    digits.insert(0, 1)
            else:
                digits[len(digits) - i - 1] += 1
                break
        
        return digits
