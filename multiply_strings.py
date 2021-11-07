class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n: int = len(num1)
        m: int = len(num2)
        rows: List[int] = []
        
        if n < m:
            num1, num2 = num2, num1
            n, m = m, n
             
        remember: int = False

        for i in range(m - 1, -1, -1):
            mult: int = int(num1[-1]) * int(num2[i])
            current_number: int = (mult + remember) % 10
            power: int = 10
            remember = mult // 10
            for j in range(n - 2, -1, -1):
                mult = int(num1[j]) * int(num2[i])
                current_number = ((mult + remember) % 10) * power + current_number
                power *= 10
                remember = (mult + remember) // 10
            rows.append(remember * power + current_number)
            remember = 0
        
        power: int = 10
        for i in range(1, len(rows)):
            rows[i] *= power
            power *= 10
        
        return str(sum(rows))
