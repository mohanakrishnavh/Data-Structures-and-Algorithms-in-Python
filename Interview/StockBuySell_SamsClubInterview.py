
'''
stock_prices = [1,3,4,1,3]
[Buy,Buy,Sell,Buy,Sell]

Buy at most one stock per day
maximum profit

'''

import heapq
from copy import deepcopy

def max_profit(stock_prices):
    flag = [False] * len(stock_prices)
    stock = deepcopy(stock_prices)
    stock_prices.sort()

    total = 0
    for i in range(len(stock_prices)-1):
        item = stock_prices.pop()
        idx = stock.index(item)
        print("idx",idx)
        print("item",item)
        flag[idx] = True
        cost = 0
        count = 0
        for j in range(idx):
            if flag[j] is False:
                cost += stock[j]
                count += 1
                print("cost",cost)
                print("count",count)
                #print("Cost:",cost)
            else:
                #print("Max_value",stock[idx])
                continue
            flag[j] = True
        sell_cost = stock[idx]
        total += (count*sell_cost) - cost
        print("total",total)

    print("Flag:",flag)
    return total

print(max_profit([1,3,4,1,2]))



