class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        changes = []
        for i in range(1, len(prices)):
            changes.append(prices[i] - prices[i - 1]
        
        max_profit = changes[0]
        max_right = max_profit
        
        for price in prices[1:]:
            max_right = max(max_right + price, price)
            max_profit = max(max_right, max_profit)
        return max_profit
        