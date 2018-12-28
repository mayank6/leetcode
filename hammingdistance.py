class Solution:
    def hammingDistance(self, x, y):
        d=0
        x=list(bin(x).replace("b",""))
        y=list(bin(y).replace("b",""))
        if len(x)==len(y):    
            for i,j in zip(x,y):        
                if int(i)!=int(j):
                    d+=1
        elif len(x)>len(y):
            for i in range(len(x)-len(y)):
                y.insert(0,"0")
            for i,j in zip(x,y):        
                if int(i)!=int(j):
                    d+=1
        else:
            for i in range(len(y)-len(x)):
                x.insert(0,"0")
            for i,j in zip(x,y):        
                if int(i)!=int(j):
                    d+=1
        return d
#------------------------------------------------------------------------------#
x=bin(x^y).count('1')
