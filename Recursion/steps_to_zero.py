def stepsToZero(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return 1 + stepsToZero(n // 2)
    else:
        return 1 + stepsToZero(n - 1)


n = int(input())

print(stepsToZero(n))
