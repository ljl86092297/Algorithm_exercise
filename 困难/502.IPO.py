from heapq import nlargest, heappush, heappop
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(nlargest(k, profits))

        n = len(profits)
        data = [(profits[i],capital[i]) for i in range(n)]

        d = sorted(data, key=lambda x:x[1])
        available = []
        while k:
            # 因为available【0】为最小值，所以用负号。
            while d and d[0][1] <= w:
                heappush(available, -d.pop(0)[0])
            if available:
                w -= heappop(available)
            else:
                break
            k -= 1
        return w