# 贪心算法
# 下一次的起点就是本次起点到终点范围内能跳到的最远距离。
class Solution:
	def jump(self, nums) -> int:
		start_j = 0
		max_j = nums[0]
		jumps_c = 1
		if len(nums) == 1:
			return 0
		for i in range(len(nums)):
			if max_j >= len(nums) - 1:
				return jumps_c
			for j in range(start_j + 1, max_j + 1):
				if nums[j] + j > max_j:
					max_j = nums[j] + j
					start_j = j
				else:
					pass
				if max_j >= len(nums) - 1:
					return jumps_c+1

			jumps_c += 1