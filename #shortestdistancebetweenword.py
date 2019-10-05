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
        
#DP SOlution by Himanshu.      
def EditDistance(word1,word2):
    n1 = len(word1)
    n2 = len(word2)
    dp = [[0 for i in range(n2+1)] for _ in range(n1+1)]
    for i in range(n2+1):
        dp[0][i] = i
    for i in range(n1+1):
        dp[i][0] = i
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if word1[i-1]==word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
    return dp[n1][n2]

print(EditDistance("abc","yabd"))
