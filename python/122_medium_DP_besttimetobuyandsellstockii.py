class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        holdlast = 0 - prices[0]
        freelast = 0

        for i in prices[1:]:
            # holdlast = max(holdlast, freelast - i)
            # freelast = max(holdlast, holdlast + i)
            hold = max(holdlast, freelast - i)
            free = max(freelast, holdlast + i)
            holdlast = hold
            freelast = free

        return free

if __name__ == '__main__':
    data = [7, 1, 5, 3, 6, 4]
    profit = Solution().maxProfit(data)
    print 'max profit is {}'.format(profit)