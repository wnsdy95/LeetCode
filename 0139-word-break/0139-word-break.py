
    
def fun(s,dc,memo):
    if(memo[s]==1):
        return False
    if(dc[s]==1):
        return True
    for i in range(len(s)+1):
        # print("dc: ",dc)
        # print("memo: ",memo)
        if(dc[s[:i]]==1):
            a=fun(s[i:],dc,memo)
            if(a):
                return True
    memo[s]=1
    return False
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dc=defaultdict(lambda:0)
        memo=defaultdict(lambda:0)
        for w in wordDict:
            dc[w]=1
        return(fun(s,dc,memo))
        