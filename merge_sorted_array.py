class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """        
        if m != 0 and n == 0:
            return
        if m == 0 and n != 0:
            for i in range(n):
                nums1[i] = nums2[i]
        
        i = 0
        j = 0
        insert_index = n + m - 1

        while i < m and j < n:
            if nums2[n - 1 - j] >= nums1[m - 1 - i]:
                nums1[insert_index] = nums2[n - 1 - j]
                nums2[n - 1 - j] = 0
                j += 1
                insert_index -= 1
            else:
                nums1[insert_index] = nums1[m - 1 - i]
                nums1[m - 1 - i] = 0
                i += 1
                insert_index -= 1
                
        if j < n:
            for k in range(n - 1 - j, -1, -1):
                nums1[insert_index] = nums2[k]
                insert_index -= 1    
                j += 1     
            
        
