class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        i = 0
        stack = []
        for e in pushed:
            stack.append(e)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i +=1
        return i == len(popped)
                
                    