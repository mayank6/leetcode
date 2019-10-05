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
    
    
#SOLUTION BY HIMANSHU - EFFICIENT USING SET
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==0 and len(t) ==0:
          return True
        elif len(s)==len(t):
          p=set(s)
          q=set(t)


          if p==q:
            for i in p:
                if s.count(i)==t.count(i):
                     return True
                else:
                     return False
          else:
             return False
        else:
            return False
