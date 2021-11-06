class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        subarrays_sum: int = sum(arr)
            
        if len(arr) < 3:
            return subarrays_sum
        
        current_sum: int = sum(arr[:3])
        subarrays_sum += current_sum

        for i in range(3, len(arr), 2):
            for j in range(i, len(arr)):
                current_sum = current_sum - arr[j - i] + arr[j]
                subarrays_sum += current_sum
            if len(arr) >= i + 2:
                current_sum = sum(arr[:(i + 2)])
                subarrays_sum += current_sum
        
        return subarrays_sum
            
