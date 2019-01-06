prev=0
x=str(bin(6)).replace("0b","")
highest=0
for i,j in enumerate(x):
    if j=="1":

        highest=max(highest,i-prev)
        prev=i
