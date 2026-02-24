def productOfDigits(n):
    if n < 10:
        return n
    return (n % 10) * productOfDigits(n // 10)


n = int(input())
print(productOfDigits(n))
