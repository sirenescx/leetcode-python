class Solution:
    def makeEqual(self, words: List[str]) -> bool:
#         if len(words) == 1:
#             return True
        
#         letters_count: Counter = Counter()
#         for word in words:
#             letters_count += Counter(word)

#         for letter in letters_count:
#             count = letters_count[letter]
#             if count < len(words) or count % len(words) != 0:
#                 return False
        
#         return True

        all_words: str = ''
        for word in words:
            all_words += word
        for char in set(all_words):
            if all_words.count(char) % len(words) != 0:
                return False
            
        return True
