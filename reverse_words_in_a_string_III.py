class Solution:
    def reverse(self, chars: List[str]):
        i: int = 0
        j: int = len(chars) - 1
        
        while i < j:
            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1
        
    def reverseWords(self, s: str) -> str:
        # return ' '.join([i[::-1] for i in s.split()])        
        word: List[str] = []
        result: str = ''
        
        for c in s:
            if c == ' ':
                self.reverse(word)
                result += ''.join(word)
                result += ' '
                word.clear()
            else:
                word.append(c)
                
        self.reverse(word)
        result += ''.join(word)
        
        return result
