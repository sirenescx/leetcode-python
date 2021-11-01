class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count_strings: dict = {}
        for i, string in enumerate(arr):
            if string not in count_strings:
                count_strings[string] = [1, i]
            else:
                count_strings[string][0] += 1
        
        count: int = 0
        index: int = 0
        for key in count_strings:
            if count_strings[key][0] == 1:
                count += 1
                if count == k:
                    index = count_strings[key][1]
        
        if count < k:
            return ''
        
        return arr[index]
