words = ["practice", "makes", "perfect", "coding", "makes"]
i1,i2=None,None
w1 = "coding"
w2 = "practice"
mini=len(words)
for i,word in enumerate(words):
    if word==w1:
        i1=i
    elif word==w2:
        i2=i
    else:
        pass
    if i1 is not None and i2 is not None:    
        mini= min(mini,abs(i1-i2))
        
        
