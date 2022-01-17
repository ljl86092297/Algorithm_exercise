class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n< 2:
            return s

        dp = [[False] * n for _ in range(n)]

        max_len = 1
        begin = 0
        for i in range(n):
            dp[i][i] = True
        # 回文子串的长度从2开始
        for L in range(2, n+1):
            #每次都从0开始遍历
            for i in range(n):
                # 左边界i每次都由遍历得来，右边界j由左边界加回文子串的长度-1
                j = L + i -1

                if j>=n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    # 当回文子串长度小于4的时候，左边界等于右边界时 一定为回文子串
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        # 如果子串是回文 那就是回文， 不是回文那就不是回文
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and L > max_len:
                    max_len = L
                    begin = i

        return s[begin: begin + max_len]


