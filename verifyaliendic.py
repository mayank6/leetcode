class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d={}
        j=0
        for i in order:
           d[i]=j 
           j+=1
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            for k in range(min(len(w1),len(w2))):
                if w1[k]!=w2[k]:
                    if d[w1[k]]>d[w2[k]]:
                        return False
                    break
            else:
                if(len(w1))>len(w2):
                    return False
        return True
