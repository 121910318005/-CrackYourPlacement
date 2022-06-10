'''
#Leet code Approach-1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit, max_profit = float('inf'), 0
        for i in prices:
            min_profit = min(i, min_profit)
            diff = i-min_profit
            max_profit = max(diff, max_profit)
        return max_profit
'''

prices = list(map(int, input().split(' ')))
min_prof=10000000
max_prof=0
for i in prices:
  min_prof=min(i, min_prof)
  diff = i-min_prof
  max_prof=max(diff, max_profit)
print('Max profit gained: ',max_profit)


# Approach-2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0,1
        m=0
        while j<len(prices):
            if prices[i]>prices[j]:
                i = j
            else:
                if prices[j]-prices[i]>m:
                    m = prices[j]-prices[i]
            j+=1
        return m
