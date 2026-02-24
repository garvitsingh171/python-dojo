def digitsInNum(n):
    if n < 10:
        return 1
    return 1 + digitsInNum(n//10)


n = int(input())

print(digitsInNum(n))
