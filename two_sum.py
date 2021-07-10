class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        answer = []
        for i in range(len(nums)):
            cur = target - nums[i]
            if cur in dictionary:
                answer.append(dictionary[cur])
                answer.append(i)
            dictionary[nums[i]] = i
        
        return answer
