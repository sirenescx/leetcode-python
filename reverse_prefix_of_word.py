class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index: int = 0
            
        for char in word:
            if char != ch:
                index += 1
            else:
                break
        
        if index == len(word) and word[index - 1] != ch:
            return word
        
        return word[:index + 1][::-1] + word[index + 1:]
