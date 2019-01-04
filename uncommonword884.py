class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a=A+" "+B
        ans=[]
        for i in a.split():
            if a.split().count(i)==1:
                ans.append(i)
        return ans
        
