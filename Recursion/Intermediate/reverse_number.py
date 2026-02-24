# Without using string conversion.

# Way-01

def reverseNum(n):
    if n < 10:
        print(n)
        return
    num = 0
    print(((num*10) + (n % 10)), end='')
    reverseNum(n//10)


# Way-02

def revNum(n, digits):
    if n == 0:
        return 0
    return (n % 10) * (10 ** (digits - 1)) + revNum(n // 10, digits - 1)


n = int(input())

reverseNum(n)
