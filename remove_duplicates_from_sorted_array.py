class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        insert_pos = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[insert_pos]:
                insert_pos += 1
                nums[insert_pos] = nums[i]

        return insert_pos + 1
