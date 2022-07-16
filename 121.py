class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_price = sys.maxsize   #최대값은 최소값으로, 최소값은 시스템 최대값으로 초기화해놓아야 이후에 정상적으로 교체가 가능
        
        for price in prices:
            min_price = min(min_price,price)    
            profit = max(profit, price - min_price)     #최대 이익 갱신
            
        return profit
