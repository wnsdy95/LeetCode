class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0
        dp = [0]*len(prices)
        for i in range(len(prices)):
            if i == 0:
                dp[0] = prices[0]
                
            elif i > 0:
                if dp[0] >= prices[i]:
                    dp[0] = prices[i]
                    if i > 1:
                        dp[i] = dp[i-1]
                    
                elif dp[0] < prices[i]:
                    if i == 1:
                        dp[i] = prices[i] - dp[0]
                    elif i > 1:
                        dp[i] = max(prices[i] - dp[0], dp[i-1])
                        
        return dp[-1]
        # buy = prices[0]
        # profit = 0
        # for i in prices[1:]:
        #     if i - buy > 0:
        #         profit = max(profit, i - buy)
        #     else:
        #         buy = i
        # return profit