class Solution:
	def threeSum(self, nums):

		nums.sort()
		# nums = list(set(nums))
		if len(nums) <= 2:
			return []
		ans = []
		# l_f, r_f = 1, len(nums)-1
		o_a = nums[0]
		for i in range(len(nums)-2):
			a = nums[i]
			if a == o_a and i != 0:

				continue
			l_f = i+1
			r_f = len(nums) -1

			while l_f < r_f:

				b = nums[l_f]
				c = nums[r_f]

				if a + b > -c:
					r_f -= 1
				elif a + b == -c:
					ans.append([a,b,c])
					while b== nums[l_f] and l_f < len(nums)-1:
						l_f += 1
					while c == nums[r_f] and r_f > 0:
						r_f -= 1

				elif a + b < -c:
					l_f += 1
			o_a = a
		return ans


