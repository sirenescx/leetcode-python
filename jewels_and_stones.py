class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set: set = set(list(jewels))
        stones_dict: dict = {}
            
        for stone in stones:
            if not stone in stones_dict:
                stones_dict[stone] = 1
            else:
                stones_dict[stone] += 1
            
        result: int = 0
        for jewel in jewels_set:
            if jewel in stones_dict:
                result += stones_dict[jewel]
        
        return result
