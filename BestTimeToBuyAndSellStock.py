class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = 10000000 #some random super large number
        maxProfit = 0

        for price in prices:
            if (price < minPrice):
                minPrice = price
            elif (price - minPrice > maxProfit):
                maxProfit = price - minPrice

        return maxProfit
