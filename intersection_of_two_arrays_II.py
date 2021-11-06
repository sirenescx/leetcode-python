class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        first_dict: dict = {}
        second_dict: dict = {}
            
        for num in nums1:
            if not num in first_dict:
                first_dict[num] = 1
            else:
                first_dict[num] += 1

        for num in nums2:
            if not num in second_dict:
                second_dict[num] = 1
            else:
                second_dict[num] += 1
                
        answer: List[int] = []
                
        if len(first_dict) < len(second_dict):
            for key in first_dict:
                if key in second_dict:
                    answer += [key] * min(first_dict[key], second_dict[key])
        else:
            for key in second_dict:
                if key in first_dict:
                    answer += [key] * min(first_dict[key], second_dict[key])
        
        return answer
