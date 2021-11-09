class Solution:
    def binary_search(self, nums: List[int], target: int) -> bool:
        left: int = 0
        right: int = len(nums) - 1
        while left <= right:
            mid: int = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if self.binary_search(matrix[i], target):
                return True
        
        return False
