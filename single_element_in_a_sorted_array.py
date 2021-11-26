class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left: int = 0
        right: int = len(nums) - 1
        
        if right == 0:
            return nums[0]
        if nums[left] != nums[left + 1]:
            return nums[left]
        if nums[right] != nums[right - 1]:
            return nums[right]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            
            if ((mid % 2) == 0 and nums[mid] == nums[mid + 1]) or ((mid - 1) % 2 == 0 and nums[mid] == nums[mid - 1]):
                left = mid + 1
            else:
                right = mid - 1

        return -1
