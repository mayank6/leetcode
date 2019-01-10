class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        f,l=0,len(S)-1
        x=[]
        S=list(S)
        while(f<l):
                    while not (S[f].isalpha()) and f<l:
                        f+=1
                        
                    while not (S[l].isalpha()) and f<l:
                        l-=1
                    
                    if f<l:
                        if S[f].isalpha() and S[l].isalpha():
                            S[f],S[l]=S[l],S[f]
                            f+=1
                            l-=1
        return "".join(S)
