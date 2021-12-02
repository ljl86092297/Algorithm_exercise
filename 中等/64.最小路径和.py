class Solution:
    def minPathSum(self, grid):
        row, cloums = len(grid), len(grid[0])
        dp = [[0 for i in range(cloums)] for i in range(row)]
        dp[0][0] = grid[0][0]
        for i in range(1, row):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, cloums):
            dp[0][i] = dp[0][i-1] + grid[0][i]

        for i in range(1, row):
            for j in range(1, cloums):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[-1][-1]

# 需要创建与输入数据一样的二维数组进行 状态的存储。