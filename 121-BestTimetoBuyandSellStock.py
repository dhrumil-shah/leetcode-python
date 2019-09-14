"""
121. Best Time to Buy and Sell Stock
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices) < 1):
            return 0
        maxProfit = 0
        pur_price = prices[0]
        for i in range(1,len(prices)):
            if (prices[i] < pur_price):
                pur_price = prices[i]
            else:
                if (prices[i] - pur_price  > maxProfit):
                    maxProfit = prices[i]- pur_price
                    
        return maxProfit
    
    def runtest(self):
        if (self.maxProfit([7,1,5,3,6,4]) ==5 \
            and self.maxProfit([7,6,4,3,1]) ==0 \
            and self.maxProfit([1,2]) ==1 \
            and self.maxProfit([7,6,5,4,3,2,1]) == 0 \
            and self.maxProfit([1,2,3,4,5,6,7,8,8]) == 7 \
            and self.maxProfit([1,2,3,4,5,6,7,1]) ==6 \
            and self.maxProfit([]) ==0 \
            ):
            print(True)
        else:
            prit(False)
            
sol = Solution()
sol.runtest()