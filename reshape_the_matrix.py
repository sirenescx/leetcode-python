class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        mat_i: int = 0
        mat_j: int = 0        
        res_i: int = 0
        res_j: int = 0
        m: int = len(mat)
        n: int = len(mat[0])
            
        if m * n != r * c:
            return mat
        
        mat_size: int = m * n
        reshaped: List[List[int]] = [[0] * c for i in range(r)]
        
        for i in range(mat_size):
            if res_j == c:
                res_i += 1
                res_j = 0
            
            if mat_j == n:
                mat_i += 1
                mat_j = 0
                
            reshaped[res_i][res_j] = mat[mat_i][mat_j]
            
            res_j += 1
            mat_j += 1
        
        return reshaped
