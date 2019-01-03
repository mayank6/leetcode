class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        y=str(int(bin(num).replace("b","")))
        m=""
        for i in y:
            if i=="1":
                m+="0"
            else:
                m+="1"
        k=int(m,2)
        return k 
