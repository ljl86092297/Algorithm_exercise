
# 取余数
class Solution:
    def reverse(self, x: int) -> int:
        digit = []
        if x == 0:
            return 0
        elif x>0:
            while x >= 1:
                digit.append(str(int(x%10)))
                x = x/10
        else:
            digit.append('-')
            while x <= -1:
                digit.append(str(int(10 - x%10 if x%10 >0 else 0 )))
                x = x/10


        r = "".join(digit)
        r = int(r)
        if r< -2 **31 or r > 2**31-1:
            return 0
        else:
            return r


X = Solution()
r = X.reverse(-10)
print(r)