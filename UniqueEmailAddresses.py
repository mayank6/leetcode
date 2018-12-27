class Solution:
    def numUniqueEmails(self, emails):
        a=[]
        for k in emails:
                left,right=k.split("@")
                if "+" in left:
                    left=left[:left.index("+")]
                if "." in left:
                    left=left.replace(".","")
                z=left+"@"+right
                if z in a:
                    pass
                else:
                    a.append(z)
        return(len(a))
