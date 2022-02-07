class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for i in range(len(s)+1)]
        if s[0] == '0':
            return 0
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s)+1):
            if s[i-2] == '1':
                if s[i - 1] == '0' :
                    dp[i] = dp[i - 2]
                else:
                    dp[i] = dp[i-1] + dp[i-2]
            elif s[i-2] == '2':
                if s[i - 1] == '0':
                    dp[i] = dp[i - 2]
                elif int(s[i-1 ]) > 6:
                    dp[i] = dp[i-1]
                else:
                    dp[i] = dp[i-1] + dp[i-2]
            elif s[i - 2] == '0':
                if s[i-1] == '0':
                    return 0
                else:
                    dp[i] = dp[i - 1]
            else:
                if s[i-1] == '0':
                    return 0
                else:
                    dp[i] = dp[i-1]
        return dp[-1]
