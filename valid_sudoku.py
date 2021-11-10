class Solution:
    def column(self, matrix: List[List[str]], i: int) -> List[int]:
        return [row[i] for row in matrix]
    
    def isSubBoxOk(self, matrix: List[List[str]], r_s: int, c_s: int, r_e: int, c_e: int) -> bool:
        counter: dict = {}
            
        for i in range(r_s, r_e):
            for j in range(c_s, c_e):
                val: str = matrix[i][j]
                if val != '.':
                    if val in counter:
                        return False
                    counter[val] = 1
        
        return True
    
    def isOk(self, array: List[int]) -> bool:
        counter: dict = {}
            
        for val in array:
            if val != '.':
                if val in counter:
                    return False
                counter[val] = 1
        
        return True
                

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: List[dict] = []
        columns: List[dict] = []
        sub_boxes: List[dict] = []
            
        for i in range(len(board)):
            if not self.isOk(board[i]):
                return False
            if not self.isOk(self.column(board, i)):
                return False
        
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                if not self.isSubBoxOk(board, i, j, i + 3, j + 3):
                    return False
                
        return True
