class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
#         x: int = 0
#         for i in range(len(nums)):
#             x ^= nums[i]
            
#         set_nums: set = set(nums)
#         answer: List[int] = []
        
#         for i in range(len(nums)):
#             if (nums[i] ^ x) in set_nums:
#                 answer.append(nums[i])
        
#         return answer

        xor: int = 0
        for i in range(len(nums)):
            xor ^= nums[i]
        
        mask: int = xor & (-xor)
        first: int = 0
        second: int = 0
        
        for i in range(len(nums)):
            if mask & nums[i] == 0:
                first ^= nums[i]
            else:
                second ^= nums[i]
        
        return [first, second]
