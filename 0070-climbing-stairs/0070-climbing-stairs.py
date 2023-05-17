class Solution(object):
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
#         def recurr(self, m, sol, n):
#             if m != n:
#                 if m + 1 == n:
#                     sol += 1
#                 return recurr(self,m + 1, sol,n)

#             if m != n:
#                 if m + 2 == n:
#                     sol += 1
#                 return recurr(self,m + 2, sol,n)
#         m = 0
#         sol = 0
        
       
#         m, sol = recurr(self, m, sol, n)

#         return sol
        if n == 0 or n == 1:
            return 1
        dp =[0] * (n+1)
        dp[0]=1
        dp[1]=1

        for i in range(2, n+1):
       
            dp[i] = dp[i-1] + dp[i-2];
       

        return dp[n];
        