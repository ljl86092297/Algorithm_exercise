
# 用dp[i][j]存储s前i个字符，与模式j前j个字符的匹配情况。
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[True] * (len(p) + 1)for i in range(len(s)+1)]
        for i in range(1, len(s)+1):
            dp[i][0] = False
        X_flag = True
        for j in range(1, len(p)+1):
            if p[j-1] != "*":
                X_flag = False
            if X_flag:
                dp[0][j] = True
            else:
                dp[0][j] = False

        for i, zifu in enumerate(s):
            i = i + 1
            for j, moshi in enumerate(p):
                j = j+1
                if moshi == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif moshi == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] and zifu == moshi
        return dp[-1][-1]


s = 'cb'
p = '?a'
S = Solution()
S.isMatch(s, p)