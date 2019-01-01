class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        x=s.split()
        for i in range(len(x)):
            x[i]=x[i][::-1]
        return (" ".join(x))
            
