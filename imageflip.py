class Solution:
    def flipAndInvertImage(self, A):
        #reversing image vectors
        for i in range(len(A)):
            n=len(A[i])
            f=0
            l=n-1
            while(True):
                A[i][f],A[i][l]=A[i][l],A[i][f]
                f+=1
                l-=1
                if(l<=f):
                    break
            for j in range(n):
                if (A[i][j]==1):
                    A[i][j]=0
                else:
                    A[i][j]=1
        return A
