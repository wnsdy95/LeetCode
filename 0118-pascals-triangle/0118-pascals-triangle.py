class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        arr =[]
        c=0
        while len(arr) < numRows:
            if len(arr) == 0:
                arr.append([1])
            elif len(arr) == 1:
                arr.append([1,1])
            else:
                tmp=[]
                for i in range(len(arr)):
                    if len(tmp) == 0:
                        tmp.append(1)
                    if i == len(arr[-1])-1:
                        tmp.append(1)
                    print("i: ",i, i+1, len(arr[-1])-1)
                    if i != len(arr[-1])-1 and len(tmp) != 0:
                        print(c,i,len(arr))
                        print(arr)
                        tmp.append(arr[-1][i]+arr[-1][i+1])
                arr.append(tmp)
            c+=1
        return arr