# class Solution:
#     def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
#         result: List[List[int]] = []
#         row_elements: int = 0
#         index: int = 0
            
#         if m * n != len(original):
#             return []
            
#         for i in range(len(original)):
#             if row_elements == 0:
#                 result.append([original[i]])
#             else:
#                 result[index].append(original[i])
#             row_elements += 1
#             if row_elements == n:
#                 row_elements = 0
#                 index += 1
        
#         return result

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result: List[List[int]] = [[]]
        row_elements: int = 0
        index: int = 0
            
        if m * n != len(original):
            return []
            
        for i in range(len(original)):
            result[index].append(original[i])
            row_elements += 1
            if row_elements == n:
                row_elements = 0
                index += 1
                if index != m:
                    result.append([])
        
        return result
