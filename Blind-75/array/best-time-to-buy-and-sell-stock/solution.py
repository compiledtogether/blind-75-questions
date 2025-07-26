# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

def maxProfit(prices: list) -> int:
    buy = prices[0]
    profit = 0
    
    for index in range(1, len(prices)):
        if(prices[index] > buy):
            if profit < (prices[index] - buy):
                profit = prices[index] - buy
        else:
            buy = prices[index]
            
    return profit

# # Test Cases

# prices1 = [7,1,5,3,6,4]
# output1 = 5

# prices2 = [7,6,4,3,1]
# output2 = 0

# print(maxProfit(prices=prices1) == output1)
# print(maxProfit(prices=prices2) == output2)