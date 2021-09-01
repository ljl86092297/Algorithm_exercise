class Solution:
    def largestPerimeter(self, nums):
        nums = sorted(nums, reverse=False)
        for i in range(len(nums)-1, 1, -1):
            print(i)
            c,b,a = nums[i],nums[i-1],nums[i-2]
            if c>=b+a:
                continue
            else:
                return c+b+a
        return 0


S = Solution()
print(S.largestPerimeter([2,1,2]))