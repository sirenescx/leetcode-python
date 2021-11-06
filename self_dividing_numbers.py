class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        numbers: List[int] = []
            
        for i in range(left, right + 1):
            number: str = str(i)
            for digit in number:
                if digit == '0' or i % int(digit) != 0:
                    break
            else:
                numbers.append(i)
                
        return numbers
            
