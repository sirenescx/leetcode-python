class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])
  
        final = [0] * len(cost)
        final[0] = cost[0]
        final[1] = cost[1]
        for i in range(2, len(cost)):
            final[i] = cost[i] + min(final[i - 2], final[i - 1])
        
        
        return min(final[-1], final[-2])
            
