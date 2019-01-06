x=list("++++")
y=x[:]
a=[]
for i in range(len(x)-1):
    if x[i]=="+" and x[i+1]=="+":
        y[i],y[i+1]="-","-"
        a.append("".join(y))
    y=x[:]
print(a)
