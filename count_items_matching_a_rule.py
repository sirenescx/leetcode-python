class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        index: int = 0 if ruleKey == 'type' else 1 if ruleKey == 'color' else 2
        count: int = 0
            
        for item in items:
            if item[index] == ruleValue:
                count += 1
        
        return count
