class Solution:
    def minTimeToType(self, word: str) -> int:
        time: int = len(word)
        pointer: int = 0
        turn: int = 0
        letter_index: int = 0
        for letter in word:
            letter_index = ord(letter) - 97
            turn = abs(letter_index - pointer)
            time += min(turn, 26 - turn)
            pointer = letter_index

        return time
  
