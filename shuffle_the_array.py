class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled: List[int] = [0] * len(nums)
        index: int = 0
            
        for i in range(0, n):
            shuffled[index] = nums[i]
            shuffled[index + 1] = nums[n + i]
            index += 2
        
        return shuffled
