class Solution:
    def peakIndexInMountainArray(self, A):
        x=len(A)
        for i in range(1,x):
            if (A[i-1]<A[i]>A[i+1]):
                return i
                
 #-----------------------------------------------------------#
 class Solution:
    def peakIndexInMountainArray(self, A):
        lo,hi=0,len(A)-1
        while lo<hi:
            mi=(lo+hi)//2
            if(A[mi]<A[mi+1]):
                lo=mi+1
            else:
                hi=mi
        return lo
