class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth: int = 0
        for i, account in enumerate(accounts):
            max_wealth = max(max_wealth, sum(account))
        
        return max_wealth
