
# 先排序 然后通过双指针，记录其中两个值减少循环。
class Solution:
	def fourSum(self, nums, target: int):
		ans = []
		if len(nums) < 4 :
			return []
		else:
			nums.sort()
			for i in range(len(nums)-3):
				if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
					break
				for j in  range(i+1, len(nums)-2):
					l_f = j+1
					r_l = len(nums)-1
					if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
						break
					elif nums[i] + nums[j] + nums[r_l] + nums[r_l-1] <target:
						continue

					while l_f < r_l:
						if nums[i] + nums[j] + nums[l_f] + nums[r_l] > target:
							r_l -= 1
						elif nums[i] + nums[j] + nums[l_f] + nums[r_l] < target:
							l_f += 1
						else:
							if [nums[i], nums[j], nums[l_f], nums[r_l]] not  in ans:
								ans.append([nums[i], nums[j], nums[l_f], nums[r_l]])
							r_l -= 1
							l_f += 1
		return ans

