class Solution:
    def repeatedNTimes(self, A):
        a={}
        for i,j in enumerate(A):
            if (j in a):
                a[j]+=1
            else:
                a[j]=1
        le=(i+1)/2
        for i in a:
             if(a[i]==le):
                return(i)
