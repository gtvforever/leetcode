class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        max_profit = 0
        min_price = prices[0]

        for i in prices[1:]:
            min_price = min(i, min_price)
            max_profit = max(i - min_price if i - min_price > 0 else 0, max_profit)

        return max_profit

if __name__ == '__main__':
    data = [7, 1, 5, 3, 6, 4]
    profit = Solution().maxProfit(data)
    print 'max profit is {}'.format(profit)