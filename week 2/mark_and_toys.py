def maximumToys(prices, k):
    prices = sorted(prices)
    sum = 0 
    count = 0 
    for i in range(len(prices)):
        sum += prices[i]
        if sum <= k:
            count += 1
    return count
prices = [1, 12, 5, 111, 200, 1000, 10]
# prices = [1, 3, 4, 8, 9, 1000, 10]

prices = []
# prices = [1, 2, 3, 4]
max_budget = 7
# max_budget = 50
print(maximumToys(prices, max_budget)) 

  # print(prices)
    # count = 0
    # index = 0
    # if(len(prices) == 0):
    #     return 0
    # if k == prices[-1]:
    #     return 1
    # sum = prices[0]
    # while sum <= k:
    #     sum += prices[count + 1]
    #     count += 1
    # return count
