class Solution:
	def maxArea(self, height):

		if len(height) < 2:
			return 0
		else:
			# 通过一个双指针，遍历数组， 用一个中间变量记录当前可容纳体积。
			max_val = 0
			l_f, r_f = 0, len(height) - 1
			while r_f > l_f:
				value = min(height[l_f], height[r_f]) * (r_f - l_f)
				if value > max_val:
					max_val = value

				if height[r_f] > height[l_f]:
					l_f += 1
				else:
					r_f -= 1
			return max_val