class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_of_nums = 0
        sum_of_all = 0
        for i in range(0, len(nums) + 1):
            sum_of_all += i
        for num in nums:
            sum_of_nums += num
        
        return sum_of_all - sum_of_nums
