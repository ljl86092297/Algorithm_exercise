class Solution:
	def searchRange(self, nums, target: int):
		if len(nums)==0:
			return [-1, -1]


		# 找左侧边界
		def left_bound():
			# 找到第一个等于target的下标， 没有就是-1
			l, r = 0, len(nums)-1

			while l < r:
				m = l + r >> 1
				if nums[m] < target:
					l = m + 1
				else:
					r = m

			return l if nums[l] == target else -1


		# 找右侧边界
		def right_bound():
			# 找到最后一个等于target的下标， 没有就是-1
			l, r, = 0, len(nums) -1

			while l < r:
				m = l+r+1 >>1
				if nums[m] > target:
					r = m - 1
				else:
					l = m

			return l if nums[l] == target else -1

		return  [left_bound(), right_bound()]


