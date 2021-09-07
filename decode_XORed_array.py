class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        new_list: List[int] = [first]
        last: int = first
        for value in encoded:
            last = last ^ value
            new_list.append(last)
        
        return new_list
