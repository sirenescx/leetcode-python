class Solution:
    def minimumMoves(self, s: str) -> int:
        x_count: int = 0
        moves: int = 0
            
        for char in s:
            if char == 'X':
                x_count += 1
                if x_count == 3:
                    moves += 1
                    x_count = 0
            else:
                if x_count != 0:
                    x_count += 1
                    if x_count == 3:
                        moves += 1
                        x_count = 0
                else:
                    continue
        
        if x_count != 0:
            moves += 1
        
        return moves
