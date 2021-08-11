class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number = 0
        for i in range(len(columnTitle)):
            number = number * 26 + (ord(columnTitle[i]) - 65 + 1) 
    
        return number
