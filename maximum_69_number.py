class Solution:
    def maximum69Number (self, num: int) -> int:
        # return int((str(num).replace('6', '9', 1)))
        new_num: int = num
        index: int = 0
        six_index: int = -1
            
        while new_num > 0:
            if new_num % 10 == 6:
                six_index = index
            new_num //= 10
            index += 1

        if six_index == -1:
            return num
        
        return num + 3 * 10 ** six_index 
