class Solution:
    def sortArrayByParity(self, A):
        n=len(A)
        a1,a2,a=0,n-1,[0]*n      
        for i in range(n):
            if(A[i]%2==0):
                a[a1]=A[i]
                a1+=1
            else:
                a[a2]=A[i]
                a2-=1
        return(a)
        
