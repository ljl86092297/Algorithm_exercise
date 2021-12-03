class Solution:
    def longestValidParentheses(self, s: str):
        dp = [0] * len(s)
        max_len = 0
        for i,c in enumerate(s):
            if i == 0:
                pass
            else:
                if c == ')' and s[i-1] == "(":
                    dp[i] = dp[i-2] + 2
                    max_len = max(max_len, dp[i])
                elif  c == ")" and  s[i-1] == ")":
                    if s[i - dp[i-1] - 1 ] == "(" and i - dp[i-1] - 1 >= 0 :
                        dp[i] = dp[i -1] + 2 + dp[i - dp[i-1] - 2]
                        max_len = max(max_len, dp[i])
        return max_len
