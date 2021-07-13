class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
#         if len(prices) < 2:
#             return 0
        
#         max_index = 0
#         profit = [0] * len(prices)
#         profit[0] = prices[1] - prices[0]
#         max_profit = profit[0]
#         for i in range(1, len(prices)):
#             current_profit = prices[i] - prices[i - 1]
#             profit_with_max_index = prices[i] - prices[max_index]
#             if profit_with_max_index > current_profit:
#                 profit[i] = profit_with_max_index
#                 if profit_with_max_index > max_profit:
#                     max_profit = profit_with_max_index
#             else:
#                 profit[i] = current_profit
#                 if current_profit >= max_profit:
#                     max_profit = current_profit
#                     max_index = i - 1
#             if prices[i - 1] < prices[max_index]:
#                 max_index = i - 1
    
#         return max_profit if max_profit > 0 else 0

        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        
        return max_profit
            
            
        
