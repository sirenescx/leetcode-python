class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        occurences: dict = {}
        good_pairs: int = 0
            
        for num in nums:
            if not num in occurences:
                occurences[num] = 1
            else:
                occurences[num] += 1

        for occurence in occurences:
            good_pairs += occurences[occurence] * (occurences[occurence] - 1) // 2
        
        return good_pairs
