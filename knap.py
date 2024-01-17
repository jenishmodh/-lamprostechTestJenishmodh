weights = list(map(int, input("Enter the weights: ").split()))
values = list(map(int, input("Enter the values: ").split()))
weight_limit = int(input("Enter the weight limit: "))

n = len(weights)
table = [[0 for x in range(weight_limit + 1)] for x in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, weight_limit + 1):
        if weights[i - 1] <= j:
            table[i][j] = max(
                values[i - 1] + table[i - 1][j - weights[i - 1]], table[i - 1][j]
            )
        else:
            table[i][j] = table[i - 1][j]

print("Maximum value achievable:", table[n][weight_limit])
