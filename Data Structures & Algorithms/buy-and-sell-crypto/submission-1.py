class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        pmin = prices[0]
        profit = 0

        for i in range(1, len(prices)):

            if prices[i - 1] < pmin:
                pmin = prices[i - 1]

            cur = prices[i] - pmin 
            print(cur)

            if cur > profit:
                profit = cur 

        if profit < 0: 
            return 0 

        else: 
            return profit 



        

            








    
            

        