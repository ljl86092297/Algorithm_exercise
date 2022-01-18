# 关键就是找到第i个元素左右两边最高的高度的最小值  减去i的高度就是水滴的高度。  然后用leftmax， rightmax 记录i左右两边的最高的高度
class Solution:
	def trap(self, height) -> int:
		leftmax, rightmax = [0] * len(height), [0] * len(height)
		for i, h in enumerate(height):
			if i == 0:
				leftmax[i] = h
			else:
				leftmax[i] = max(leftmax[i - 1], h)

		for i in range(len(height) - 1, -1, -1):
			if i == len(height) - 1:
				rightmax[i] = height[i]
			else:
				rightmax[i] = max(rightmax[i + 1], height[i])
		drops = 0
		for i in range(1, len(height) - 1):
			drops += min(leftmax[i], rightmax[i]) - height[i]
		return drops
