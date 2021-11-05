class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum: int = max(candies)
        result: List[bool] = [True] * len(candies)
        for i, candy in enumerate(candies):
            if candy + extraCandies < maximum:
                result[i] = False
        
        return result
