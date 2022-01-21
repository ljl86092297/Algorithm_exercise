
# 对word1的删除就是对word2的插入。
# word到空字符串的编辑距离就是word的长度。
# word1的第i 个字符到 word2的第j个字符的最短编辑距离 就等于
# ①word1的i-1个字符到word2的第j个字符的最短编辑距离 + word1插入一个字符。
# ②word1的i个字符到word2的第j-1个字符的最短编辑距离 + word2插入一个字符。
# ③word1的i -1 个字符到 word2的第j-1个字符的最短编辑距离 + 修改word1或者word2的一个字符， 如果word1的第i个与word2的第j个字符相等 就不需要修改。
# 取上述最短的一个编辑距离。
class Solution:
	def minDistance(self, word1: str, word2: str) -> int:
		if len(word1) == 0:
			return len(word2)
		if len(word2) == 0:
			return len(word1)

		dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]

		for i in range(len(word1) + 1):
			dp[0][i] = i
		for i in range(len(word2) + 1):
			dp[i][0] = i

		for i in range(1, len(word2) + 1):
			for j in range(1, len(word1) + 1):
				if word2[i - 1] == word1[j - 1]:
					dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])
				else:
					dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
		return dp[-1][-1]
