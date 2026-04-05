import math


def koko_banana(piles, h):
    low = 1
    high = max(piles)
    result = high

    while low <= high:
        k = (low + high) // h

        total_hr = 0

        for pile in piles:
            total_hr += math.ceil(pile/k)

        if total_hr <= h:
            result = k
            high = k - 1
        else:
            low = k + 1

    return result


piles = list(map(int, input().split()))

h = int(input())

print(koko_banana(piles, h))
