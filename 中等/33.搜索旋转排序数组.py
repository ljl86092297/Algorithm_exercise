
# 直接二分法就行  因为每次二分 总有一部分是有序数组。
class Solution:
	def search(self, nums, target):
		if len(nums) == 0:
			return -1
		else:
			l ,r = 0, len(nums) -1
			while l <=r :
				mid = int((r+l)/ 2)

				if nums[mid] == target:
					return mid

				if nums[l] <= nums[mid]:
					if nums[mid] > target >= nums[l]:
						r = mid -1
					else:
						l = mid + 1

				else:
					if nums[mid] < target <=  nums[r]:
						l = mid + 1
					else:
						r = mid - 1
		return -1