def knapsack(weights, values, weight_limit):
    n = len(weights)
    dp = [[0] * (weight_limit + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(weight_limit + 1):
            # If the current item can fit in the knapsack
            if weights[i - 1] <= w:
                # Choose the maximum value between including and excluding the current item
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                # If the current item cannot fit, exclude it
                dp[i][w] = dp[i - 1][w]

    # The result is stored in the bottom-right cell of the table
    return dp[n][weight_limit]

# Take user input for weights, values, and weight limit
weights = list(map(int, input("Enter the weights separated by space: ").split()))
values = list(map(int, input("Enter the values separated by space: ").split()))
weight_limit = int(input("Enter the weight limit: "))

# Calculate and print the result
result = knapsack(weights, values, weight_limit)
print("Maximum value achievable:", result)
