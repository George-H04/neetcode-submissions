class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest_seen = prices[0]

        for n in prices:
            if n < lowest_seen:
                lowest_seen = n
            else:
                profit = max(profit, n - lowest_seen)

        return profit
                