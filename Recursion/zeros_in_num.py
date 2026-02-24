def zerosInNum(n):
    if n == 0:
        return 0
    return (1 if n % 10 == 0 else 0) + zerosInNum(n//10)


n = int(input())
print(zerosInNum(n))
