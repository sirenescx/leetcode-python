class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)
    
#         left: int = 0
#         right: int = n
        
#         while left <= right:
#             mid = (left + right) // 2
#             current = mid * (mid + 1) // 2;
#             if current == n:
#                 return mid
#             if n < current:
#                 right = mid - 1
#             else:
#                 left = mid + 1
        
#         return int(right)
            
