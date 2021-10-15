class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_ditt = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0
        strid = 0
        f = True
        for i in range(len(s)-1):
            if strid >0:
                strid -=1
                f = True
                continue
            if s_ditt[s[i]] < s_ditt[s[i+1]]:
                f = False
                strid += 1
                sum += s_ditt[s[i+1]]- s_ditt[s[i]]
            else:
                f = True
                sum += s_ditt[s[i]]
        if f == True:
            sum += s_ditt[s[-1]]
        return sum




