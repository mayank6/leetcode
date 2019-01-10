class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        a=S.split()
        t=""
        vowel=["a","e","i","o","u"]
        for i,j in enumerate(a):
            if j[0].lower() in vowel:
                j+="ma"
                j+="a"*(i+1)
                a[i]=j
            else:
                t=j[0]
                j=j[1:]
                j+=t
                j+="ma"
                j+="a"*(i+1)
                a[i]=j

        return " ".join(a)
