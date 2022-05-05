'''
#Leet code
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
