x="listen"
y="silent"
a=[]
for i,j in enumerate(x):
    a.append(j)
length=i+1
for j in y:
    if j in a:
        length-=1
if length==0 and len(x)==len(y):
    print("Anagram")
else:
    print("Not anagram")
