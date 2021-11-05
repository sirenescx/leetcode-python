class Solution:
    def sortSentence(self, s: str) -> str:
        words: List[str] = [''] * 10
        word: str = ''
        for i in range(len(s)):
            if s[i].isalpha():
                word += s[i]
            elif s[i].isdigit():
                words[int(s[i]) - 1] = word
                word = ''
                
        for i in range(len(words)):
            if words[i] != '':
                if not word == '':
                    word += ' '
                word += words[i]
        
        return word
