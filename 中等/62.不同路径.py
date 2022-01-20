
# dp[m][n] 的格子走法数由 上边格子走法加左边格子走法得到。
class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		if m == 1 or n == 1:
			return  1
		dp = [[0] * n for _ in range(m)]
		for i in range(m):
			for j in range(n):
				if i == 0 or j == 0:
					dp[i][j] = 1
				else:
					dp[i][j] = dp[i-1][j] + dp[i][j-1]
		return dp[m-1][n-1]