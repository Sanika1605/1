def knapsack(values,weight,capacity):
    n=len(values)
    dp=[[0 for _ in range(capacity+1)]for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,capacity+1):
            if weight[i-1]<=w:
                dp[i][w]=max(dp[i-1][w],values[i-1]+dp[i-1][w-weight[i-1]])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][capacity]

values=[100,120,90]
weight=[20,10,30]
capacity=50
final_val=knapsack(values,weight,capacity)
print(final_val)