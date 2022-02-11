class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        n = len(nums)
        if n< 3:
            return 0
        d ,t  = nums[0] - nums[1], 0
        ans = 0
        for i in range(2, n):
            if nums[i-1] - nums[i] == d:
                t += 1
            else:
                d = nums[i-1] - nums[i]
                t = 0
            ans += t
        return ans
