class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        a=dict()
        b=set()
        w=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i,j in enumerate(w,97):
            a[chr(i)]=j
        for i in words:
            s=""
            for j in i:
                s+=a[j]
            b.add(s)
        return(len(b))       
