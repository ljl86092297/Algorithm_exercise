class Solution:
    def firstMissingPositive(self, nums) -> int:
        L = len(nums)
        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = L + 1
        # print(nums)
        # for num in nums:
        #     print(num)
        for i, num in enumerate(nums):
            num = abs(num)
            if num <= L:
                nums[num - 1] = -abs(nums[num - 1])

        for i, num in enumerate(nums):
            if num > 0:
                return i + 1
        return L + 1

S =   Solution()
S.firstMissingPositive([3,4,-1,1])