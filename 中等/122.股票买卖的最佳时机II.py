
# 我这里用了双指针，  也可以用动态规划。
class Solution:
    def maxProfit(self, prices) -> int:
        buy_f = 0
        sell_f =  1
        profit = 0
        if len(prices) <= 1:
            return 0
        else:
            while sell_f < len(prices):
                if prices[buy_f] >= prices[sell_f]:
                    buy_f +=1
                    sell_f +=1
                elif prices[buy_f] < prices[sell_f]:
                    if sell_f >= len(prices) -1:
                        profit += prices[sell_f] - prices[buy_f]
                        sell_f += 1
                    else:
                        if prices[sell_f+1] > prices[sell_f]:
                            sell_f +=1
                        else:
                            profit += prices[sell_f] - prices[buy_f]
                            buy_f = sell_f+1
                            sell_f += 2
        return profit


S = Solution()
x = S.maxProfit([1,2,3,4,5])
print(x)