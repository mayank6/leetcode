def ispallind(s):
    a=set()
    for i in s:
        if i in a:
            a.remove(i)
        else:
            a.add(i)
    return len(a)<=1
x=ispallind("abaaba")
