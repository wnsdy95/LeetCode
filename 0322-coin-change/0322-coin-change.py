
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


        # dp[i] := fewest # Of coins to make up i
        dp = [0] + [amount + 1] * amount

        for coin in coins:
          for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
            # print(dp)

        return -1 if dp[amount] == amount + 1 else dp[amount]