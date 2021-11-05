class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average: int = sum(nums[:k])
        average: int = max_average
        
        for i in range(k, len(nums)):
            average = average + nums[i] - nums[i - k]
            max_average = max(max_average, average)
                
        return max_average / k
