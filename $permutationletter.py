S = "3z4abc"
def letterCasePermutation(S):
    ans = []
 
    def dfs(S, i, n):
      if i == n:
        ans.append(''.join(S))
        return
      
      dfs(S, i + 1, n)      
      if not S[i].isalpha(): return      
      S[i] = chr(ord(S[i]) ^ (1<<5))
      dfs(S, i + 1, n)
      S[i] = chr(ord(S[i]) ^ (1<<5)) #backtracking
    
    dfs(list(S), 0, len(S))
    return ans
print(letterCasePermutation(S))

#-----------------------------------------#
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        q=[]
        q.append("")
        level=-1
        while True:
            level+=1
            if level==len(S):
                break
            for i in range(len(q)):
                ch=S[level]
                element=q.pop(0)
                if ch.isdigit():
                    q.append("{}{}".format(element,ch))
                else:
                    q.append("{}{}".format(element,ch.lower()))
                    q.append("{}{}".format(element,ch.upper()))
        return q
    
 #USING INBUILT PYTHON LIBRARY
# Function to find permutations of a given string 
from itertools import permutations 

def allPermutations(str): 
	permList = permutations(str) 
	for perm in list(permList): 
		print (''.join(perm)) 



