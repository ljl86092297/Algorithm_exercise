class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        for i in range(min(len(v1), len(v2))):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) <int(v2[i]):
                return -1
            else:
                continue
        if len(v1) > len(v2):
            for i in range(len(v2),len(v1)):
                if int(v1[i]) > 0 :
                    return 1
                else:
                    continue
        elif len(v1) < len(v2):
            for i in range(len(v1),len(v2)):
                if int(v2[i]) > 0 :
                    return -1
                else:
                    continue
        else:
            return 0
        return  0


S =Solution()
print(S.compareVersion("1.1", "1.1.2"))