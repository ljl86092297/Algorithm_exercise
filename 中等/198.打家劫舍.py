# 最后偷窃的数一定是i或者i-1
class Solution:
	def rob(self, nums) -> int:
		dp = [0 for i in range(len(nums))]
		if len(nums) == 1:
			return nums[0]
		elif len(nums) == 2:
			return max(nums[0], nums[1])
		elif len(nums) == 3:
			return max(nums[0] + nums[2], nums[1])

		dp[0] = nums[0]
		dp[1] = nums[1]
		dp[2] = nums[0] + nums[2]
		for i in range(3, len(nums)):
			dp[i] = max(dp[i - 2] + nums[i], dp[i - 3] + nums[i])
		return max(dp[-1], dp[-2])
