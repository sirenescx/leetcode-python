class Solution:
    def reverse(self, nums: List[int], left: int, right: int) -> None:
        for i in range(left, (right + left) // 2):
            nums[i], nums[left + right - 1 - i] = nums[left + right - 1 - i], nums[i]
            
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n: int = len(nums)
        if n <= 1:
            return
        
        self.reverse(nums, 0, n)
        k %= n
        self.reverse(nums, 0, k)
        self.reverse(nums, k, n)
