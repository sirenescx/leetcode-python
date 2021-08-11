class Solution:
    def binary_search(self, numbers: List[int], target: int, index: int) -> int: 
        left = 0
        right = len(numbers) - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == target and mid != index:
                return mid
            if numbers[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
                
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            j = self.binary_search(numbers, abs(numbers[i] - target), i)
            if j != -1:
                return [i + 1, j + 1]
        
        return [0, 0]
