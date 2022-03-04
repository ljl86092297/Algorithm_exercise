class Solution:
	def permute(self, nums):
		pass
		n = len(nums)
		ans = []
		def backtrack(first):
			if first == n:
				ans.append(nums[:])
			for i in range(first, n):
				# 将要填入的数字 与当前位置进行交换，这样就代表了填入了原数组中第i个元素。
				nums[first], nums[i] = nums[i], nums[first]
				# 每次都到下一个位置 直至所有位置都被遍历
				backtrack(first+1)
				# 返回这层 要复原到原来的状态。
				nums[first], nums[i] = nums[i], nums[first]
		backtrack(0)
		return ans