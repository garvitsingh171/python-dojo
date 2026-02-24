n = int(input())

matrix1 = []

for _ in range(n):
    row1 = list(map(int, input().split()))
    matrix1.append(row1)

matrix2 = []

for _ in range(n):
    row2 = list(map(int, input().split()))
    matrix2.append(row2)

matrix3 = []

for i in range(n):
    row3 = []
    for j in range(n):
        num = 0
        for k in range(n):
            num = (matrix1[i][k]) * (matrix2[k][j])
        row3.append(num)
    matrix3.append(row3)

print(matrix3)
