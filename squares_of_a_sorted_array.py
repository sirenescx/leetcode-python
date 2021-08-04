class Solution:
    def merge(self, first: List[int], m: int, second: List[int], n: int):
        if m != 0 and n == 0:
            return first
        if m == 0 and n != 0:
            for i in range(n):
                first[i] = second[i]
            return first
        
        i = 0
        j = 0
        insert_index = n + m - 1
        
        while i < m and j < n:
            if second[n - 1 - j] >= first[m - 1 - i]:
                first[insert_index] = second[n - 1 - j]
                second[n - 1 - j] = 0
                j += 1
            else:
                first[insert_index] = first[m - 1 - i]
                first[m - 1 - i] = 0
                i += 1
            insert_index -= 1

        if j < n:
            for k in range(n - 1 - j, -1, -1):
                first[insert_index] = second[k]
                insert_index -= 1    
                j += 1   
                
        
    def sortedSquares(self, nums: List[int]) -> List[int]:
        min_by_abs = abs(nums[0])
        min_index = 0
        for i in range(1, len(nums)):
            if abs(nums[i]) < min_by_abs:
                min_by_abs = abs(nums[i])
                min_index = i

        l = 0
        r = min_index
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        size = len(nums) - min_index - 1
        nums2 = [0] * size
        l = 0
        for i in range(min_index + 1, len(nums)):
            nums2[l] = nums[i]**2
            l += 1
            nums[i] = 0

        for i in range(min_index + 1):
            nums[i] = nums[i]**2

        self.merge(nums, min_index + 1, nums2, size)

        return nums
        
