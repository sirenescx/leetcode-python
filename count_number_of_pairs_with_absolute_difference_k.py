class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums_dict: dict = {}

        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
                
        count: int = 0
        for key in nums_dict:
            if key - k in nums_dict:
                count += nums_dict[key] * nums_dict[key - k]
            if k + key in nums_dict:
                count += nums_dict[key] * nums_dict[k + key]
        
        return count // 2
