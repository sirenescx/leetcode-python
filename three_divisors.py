class Solution:
    def isThree(self, n: int) -> bool:
        if n <= 3:
            return False
        root = math.floor(math.sqrt(n))
        if root**2 != n:
            return False
        else:
            for div in range(2, root // 2):
                if n % div == 0:
                    return False
                
        return True
