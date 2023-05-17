
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
#         sol = 0
#         coins = sorted(coins)
#         for i in range(len(coins) - 1, -1, -1):
            
#             if amount / coins[i] >= 1 and amount > 0:
#                 sol += int(amount / coins[i])
#                 amount -= coins[i] * int(amount / coins[i])
#             print(i," ",sol," " ,amount)
#             print(coins[i])
#         if amount != 0:
#             return -1
#         return sol


        dp=[1e9] * (amount+1)
        dp[0]=0
        
        for coin in coins:
            for i in range(coin, amount+1):
                if i-coin>=0:
                    dp[i]=min(dp[i], dp[i-coin]+1)
        
        return -1 if dp[-1]== 1e9 else dp[-1]