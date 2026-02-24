# FlowerBed

size = int(input("Enter the size of flowerbed: "))
n = int(input("Enter the number of plants to be planted: "))
flower = list(map(int, input("Enter the flowerbed array: ").split()))

for i in range(size):
    if i == 0:
        if flower[i+1] == 0 and flower[i] == 0:
            flower[i] = 1
            n -= 1
    elif i == size-1:
        if flower[i-1] == 0 and flower[i] == 0:
            flower[i] = 1
            n -= 1
    else:
        if flower[i+1] == 0 and flower[i-1] == 0 and flower[i] == 0:
            flower[i] = 1
            n -= 1

if n == 0:
    print(True)
else:
    print(False)
