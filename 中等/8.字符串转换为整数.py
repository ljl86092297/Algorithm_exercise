
# 自动机，先生成各个状态之间转换的状态表，存储每个字符进来以后的状态来判断是否结束。
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = 1
        res = 0
        i= 0
        if len(s) == 0:
            return 0

        for a in s:
            if a == ' ':
                i+=1
            else:
                break
        start = i
        for idx in range(i, len(s)):
            if(idx == start and s[idx] == '+'):
                sign = 1
            elif( idx == start and s[idx] == '-'):
                sign = -1
            elif s[idx].isdigit():
                if (res < -2 **31/ 10 or (res == int(-2 **31 /10) and 10 -  int(s[idx])  <( -2**31 ) %10) ):
                    return -2**31
                elif res > 2**31/10 or( res == int(2**31 /10) and int(s[idx]) > (2**31-1)%10) :
                    return  2**31-1
                res = res*10 + sign *int(s[idx])
            else:
                break
        return res


S =Solution()
X = S.myAtoi("-2147483649")

print(X)