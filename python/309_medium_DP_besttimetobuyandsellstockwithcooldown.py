class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        holdlastlast = -prices[0]
        holdlast = max(holdlastlast, -prices[1])
        freelastlast = 0
        freelast = max(freelastlast, holdlastlast + prices[1])

        for i in prices[2:]:
            hold = max(holdlast, freelastlast - i)
            free = max(freelast, holdlast + i)
            holdlast = hold
            freelastlast = freelast
            freelast = free
        return freelast

if __name__ == '__main__':
    data = [7, 1, 5, 3, 6, 4]
    profit = Solution().maxProfit(data)
    print 'max profit is {}'.format(profit)