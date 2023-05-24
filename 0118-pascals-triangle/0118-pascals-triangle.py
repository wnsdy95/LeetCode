class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # f(2,1) = f(1,0) + f(1,1)
        # f(3,2) = f(2,1) + f(2,2)
        # f(i,j) = f(i-1, j-1) + f(i-1, j)
        # #Brute-Force
        # arr =[]
        # c=0
        # while len(arr) < numRows:
        #     if len(arr) == 0:
        #         arr.append([1])
        #     elif len(arr) == 1:
        #         arr.append([1,1])
        #     else:
        #         tmp=[]
        #         for i in range(len(arr)):
        #             if len(tmp) == 0:
        #                 tmp.append(1)
        #             if i == len(arr[-1])-1:
        #                 tmp.append(1)
        #             if i != len(arr[-1])-1 and len(tmp) != 0:
        #                 tmp.append(arr[-1][i]+arr[-1][i+1])
        #         arr.append(tmp)
        #     c+=1
        # return arr
        
        #Optimize the Code
        arr = []
        for i in range(numRows):
            arr.append([1])
            if i > 1:
                for j in range(i-1):
                    arr[i].append(arr[i-1][j]+arr[i-1][j+1])
            if i > 0:
                arr[i].append(1)
                    
        return arr
