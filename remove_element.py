class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        insert_pos = 0
        count = 0
        for i in range(0, len(nums)):
            if nums[i] != val and i != len(nums):
                nums[insert_pos] = nums[i]
                insert_pos += 1
        
        return insert_pos
                
        
