class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_coins: int = 0
        n: int = len(piles)
            
        for i in range(n - 2, n // 3 - 1, -2):
            max_coins += piles[i]
        
        return max_coins
        
