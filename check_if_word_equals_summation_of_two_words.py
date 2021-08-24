class Solution:
    def getValueOfWord(self, word: str) -> int:
        value = 0
        for letter in word:
            value = value * 10 + (ord(letter) - 97)
        
        return value
        
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        values = list(map(self.getValueOfWord, [firstWord, secondWord, targetWord]))
        
        return values[0] + values[1] == values[2]

        
