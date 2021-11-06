class Solution:
    morse_codes: List[str] = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
    def getMorseCodeValue(self, word: str) -> str:
        value: str = ''
        for char in word:
            value += self.morse_codes[ord(char) - ord('a')]
            
        return value
    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        unique: set = set()
        for word in words:
            unique.add(self.getMorseCodeValue(word))
            
        return len(unique)
        
