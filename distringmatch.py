#not for large input 
x="DDI"
l=[x for x in range(len(x)+1)]
for k in range(len(x)):
    for i in range(len(x)):
        if x[i]=="I":
            if l[i]>l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
        else:
            if l[i]<l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]

#----------------------------------------------------------------#
#for any input
l=0
h=len(x)
n=[]
for i in x:
    if i=="I":
        n.append(l)
        l+=1
    else:
        n.append(h)
        h-=1
