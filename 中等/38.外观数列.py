class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return str("1")
        else:

            inin_v = [1]
            for i in range(n-1):
                s = ""
                count = 0
                flag = inin_v[0]
                last_count = 0
                index = 0
                while index < len(inin_v) :
                    if inin_v[index] == flag:
                        count += 1
                        index += 1
                        last_count = 0
                    else:

                        s += str(index) + str(inin_v[index - 1])
                        count = 0
                        last_count = 1
                        # index -= 1
                        flag = inin_v[index]
                if last_count > 0:
                    s += str(last_count) + str(inin_v[-1])
                else:
                    s += str(count) + str(inin_v[-1])
                inin_v = s
            return s



