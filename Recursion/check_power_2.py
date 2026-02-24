def isPowerOf2(n):
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    return isPowerOf2(n // 2)


n = int(input())

print(isPowerOf2(n))
