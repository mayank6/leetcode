class Solution:
    def toLowerCase(self, str):
        s=""
        for i in str:
            if (ord(i)>=96 and ord(i)<=122):
                s+=i
            elif(ord(i)>=65 and ord(i)<=65+26):
                x=ord(i)
                s+=chr(x+32)
            else:
                s+=i
        return(s)
        
