class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        i1 = 0
        i2 = 0
        i3 = len(matrix) - 1
        i4 = len(matrix) - 1
        
        iteration = 1
        
        while i1 < len(matrix) and i2 < len(matrix) and i3 > 0 and i4 > 0 and i2 < i4:
            first = matrix[i3][i1]
            second = matrix[i1][i2]
            third = matrix[i2][i4]
            fourth = matrix[i4][i3]
        
            print(first, second, third, fourth)
            print(i1, i2, i3, i4)
            
            matrix[i3][i1] = fourth
            matrix[i1][i2] = first
            matrix[i2][i4] = second
            matrix[i4][i3] = third
            i3 -= 1
            i2 += 1
            
            if i3 == 0 or i2 == len(matrix) - iteration:
                i3 = len(matrix) - 1 - iteration
                i2 = 0 + iteration
                i4 -= 1
                i1 += 1
                iteration += 1
