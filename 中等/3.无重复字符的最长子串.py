

# 做指针跟右指针来确定滑动的窗口。
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        max_len = 0
        l = set()
        rk = 0
        n = len(s)
        for i, z in enumerate(s):
            if i != 0:
                l.remove(s[i-1])
            while rk < n and s[rk] not in l:
                l.add(s[rk])
                rk += 1
            max_len = max(max_len, rk - i)
        return max_len




