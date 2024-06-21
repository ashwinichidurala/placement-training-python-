#which day is best to acheive maximum profit by selling and purchasing a pen in a week
#ip 15 3 2 7 8 4
#   m t w t f s
#op 6
a=[3,9,8,4,1,8]
b=a[0]
def maxProfit(prices):
    sell=0
    profit=0
    temp=0
    for i in range(len(prices)-1,-1,-1):
        if prices[i]>sell:
            sell=prices[i]
        elif prices[i]<sell:
            temp=sell-prices[i]
            profit=max(profit,temp)
    return profit

        
