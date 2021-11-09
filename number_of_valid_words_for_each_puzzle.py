class Solution:
    def bitmask(self, word: str) -> int:
        mask: int = 0
        for letter in word:
            mask |= 1 << (ord(letter) - ord('a'))
        
        return mask
    
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        word_counts = Counter(self.bitmask(word) for word in words)
        answer: List[int] = [0] * len(puzzles)
            
        for i, puzzle in enumerate(puzzles):
            first_character: int = 1 << (ord(puzzle[0]) - ord('a'))
            count: int = word_counts[first_character]
            mask: int = self.bitmask(puzzle[1:])
            
            submask: int = mask
            while submask:
                count += word_counts[submask | first_character]
                submask = (submask - 1) & mask
            
            answer[i] = count
            
        return answer
