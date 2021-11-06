class Solution:
    def sumZero(self, n: int) -> List[int]:    
        half: List[int] = list(range(1, n))
        return half + [-sum(half)]
