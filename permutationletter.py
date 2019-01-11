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
