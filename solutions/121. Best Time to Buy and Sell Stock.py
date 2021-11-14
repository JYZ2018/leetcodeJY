class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_max=0
        min=prices[0]
        for i in range(1,len(prices)):
            profit=prices[i]-min
            if profit>profit_max:
                profit_max=profit
            
            if prices[i]<min:
                min=prices[i]
        return profit_max
            
        
