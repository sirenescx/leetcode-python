# Approach
Hash table for faster search

# Code
```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_index: dict = dict()
        for i, num in enumerate(nums):
            if target - num in subs:
                return [i, num_index[target - num]]
            num_index[num] = i

```
