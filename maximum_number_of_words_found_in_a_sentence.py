class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words: int = 0
        current_words: int = 1
        for sentence in sentences:
            for char in sentence:
                if char == ' ':
                    current_words += 1
            max_words = max(max_words, current_words)
            current_words = 1
        
        return max_words
                    
