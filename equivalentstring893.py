A=["abc","acb","bac","bca","cab","cba"]

def count(A):
            ans = [0] * 52
            for i, letter in enumerate(A):
                ans[ord(letter) - ord('a') + 26 * (i%2)] += 1
            return tuple(ans)

print(len({count(word) for word in A}))
