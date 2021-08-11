class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ''
        while columnNumber != 0:
            mod_26_zero = columnNumber % 26 == 0
            number = 26 if mod_26_zero else int(columnNumber) % 26
            title += chr(ord('@') + number)
            if mod_26_zero:
                columnNumber -= 1
            columnNumber //= 26
        
        return title[::-1]
