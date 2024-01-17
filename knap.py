weights = [3, 1, 4]
values = [4, 4, 1]
capacity = 5

n = len(weights)
table = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, capacity + 1):
        if weights[i - 1] <= j:
            table[i][j] = max(
                values[i - 1] + table[i - 1][j - weights[i - 1]], table[i - 1][j]
            )
        else:
            table[i][j] = table[i - 1][j]

print(table[n][capacity])
