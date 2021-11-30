class Solution:
    def generateParenthesis(self, n: int):
        if n==0:
            return []
        total_l = []
        total_l.append(None)
        total_l.append("()")
        # total_l 记录了第n组括号的所有排列组合
        for i in range(2, n+1):
            l = []
            for j in range(i):
                #每次由n-1的排列组合  与（）组合而成， 这里的i就是n 所以要再减1
                inner_list = total_l[j]
                right_list = total_l[i-j-1]
                for k1 in inner_list:
                    for k2 in right_list:
                        if k1 == None:
                            k1 = ""
                        if k2 == None:
                            k2= ""
                        # 这是核心
                        k_l = "(" + k1 + ")" + k2

                        l.append(k_l)
            total_l.append(l)
        return total_l[n]


