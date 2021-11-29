class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_left: List[int] = [1] * len(nums)
        product_right: List[int] = [1] * len(nums)
        answer: List[int] = [1] * len(nums)
        
        product_left[0] = nums[0]
        product_right[-1] = nums[-1]
        
        for i in range(1, len(nums)):
            product_left[i] = product_left[i - 1] * nums[i]
            product_right[len(nums) - i - 1] = product_right[len(nums) - i] * nums[len(nums) - i - 1]

        for i in range(1, len(nums) - 1):
            answer[i] = product_left[i - 1] * product_right[i + 1]
        
        answer[0] = product_left[-1] // nums[0] if nums[0] != 0 else product_right[1]
        answer[-1] = product_right[0] // nums[-1] if nums[-1] != 0 else product_left[-2]
        
        return answer
