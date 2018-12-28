class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        d=0
        for i in range(len(A[0])):
                    c=0
                    for j in range(0,len(A)-1):
                        if ord(A[j][i])>ord(A[j+1][i]):
                            c=1
                            break
                    if c==1:
                        d+=1
        return d

#--------------------------------------------------------------------------------#
#clean and consise

A=["cba","daf","ghi"]
ans = 0
for col in zip(*A):
            if any(col[i] > col[i+1] for i in range(len(col) - 1)):
                ans += 1
       
#-----------------------------------------------------------#

A=["cba","daf","ghi"]
d=0
for i in zip(*A):
        if sorted(i)!=list(i):
                d+=1
        return d
