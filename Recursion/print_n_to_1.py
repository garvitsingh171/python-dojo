def printNum(n):
    if n == 0:
        return
    print(n)
    printNum(n-1)


n = int(input())

printNum(n)
