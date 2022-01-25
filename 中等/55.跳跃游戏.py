# 这个就是暴力求解。
class Solution:
	def canJump(self, nums) -> bool:
		if len(nums) == 1:
			return True
		# elif len(nums) == 1 and nums[0] == 0:
		# 	return False

		max_index = nums[0]
		num_len = len(nums) -1
		for i, n in enumerate(nums):
			if i > max_index:
				return False
			else:
				max_index = max(max_index, i + n)
			if max_index >= num_len:
				return True
