class Solution:
    def maxCount(self, m: int, n: int, ops) -> int:
        min_x: int = m
        min_y: int = n
        for op in ops:
          if ops[0] < min_x:
            min_x = ops[0]
          if ops[1] < min_y:
            min_y = ops[1]

        return min_x * min_y
