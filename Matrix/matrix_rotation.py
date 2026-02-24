n = int(input())

matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix[i].reverse()


print(matrix)
