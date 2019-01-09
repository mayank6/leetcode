class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        ans=0
        def checkprime(x):
            if x==0 or x==1:
                return False
            for i in range(2,(x//2)+1):
                if x%i==0:
                    return False
            return True
        for i in range(L,R+1):
            l=bin(i).replace("0b","").count("1")
            if checkprime(l):
                ans+=1
        return ans
