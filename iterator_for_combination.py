class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters: str = characters
        self.combination_length: int = combinationLength
        self.returned_combinations: int = 0
        self.combinations: List[str] = []
        self.__dfs__(self.characters, [])
            
    def __dfs__(self, characters: str, path: List[str]):
        if len(path) == self.combination_length:
            self.combinations.append(''.join(path))
            return
        
        for i in range(len(characters)):
            self.__dfs__(characters[i + 1:], path + [characters[i]])

    def next(self) -> str:
        self.returned_combinations += 1
        return self.combinations[self.returned_combinations - 1]
        

    def hasNext(self) -> bool:
        return self.returned_combinations < len(self.combinations)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
