class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid) -> int:
		if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1:
			if obstacleGrid[0][0] == 0:
				return 1
			else:
				return 0

		dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
		for i in range(len(dp)):
			if i == 0:
				if obstacleGrid[i][0] == 0:
					dp[i][0] = 1
				else:
					dp[i][0] = 0
			else:
				if dp[i - 1][0] == 0 or obstacleGrid[i][0] == 1:
					dp[i][0] = 0
				else:
					dp[i][0] = 1

		for i in range(len(dp[0])):
			if i == 0:
				if obstacleGrid[i][0] == 0:
					dp[0][i] = 1
				else:
					dp[0][i] = 0
			else:
				if dp[0][i - 1] == 0 or obstacleGrid[0][i] == 1:
					dp[0][i] = 0
				else:
					dp[0][i] = 1
		print(dp)
		for i in range(1, len(dp)):
			for j in range(1, len(dp[0])):
				if obstacleGrid[i][j] == 1:
					dp[i][j] = 0
				else:
					dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

		return dp[-1][-1]


S = Solution()
x = S.uniquePathsWithObstacles([[0,1]])
print(x)