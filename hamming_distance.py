class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff: int = x ^ y
        distance: int = 0
        while diff > 0:
            if diff % 2 == 1:
                distance += 1
            diff //= 2
        
        return distance
