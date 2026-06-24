class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mp=0
        m=prices[0]
        for i in range(len(prices)):
            m = min(prices[i],m)
            
            mp=max(mp,prices[i]-m)
        return mp
