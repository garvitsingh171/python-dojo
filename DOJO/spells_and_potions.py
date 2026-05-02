def successfulPairs(spells, potions, success):
    potions.sort()
    m = len(potions)
    res = []

    for spell in spells:
        left = 0
        right = m - 1
        ans = m

        while left <= right:
            mid = (left + right) // 2

            if spell * potions[mid] >= success:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        res.append(m - ans)

    return res


spells = list(map(int, input().split()))
potions = list(map(int, input().split()))
success = int(input())

print(successfulPairs(spells, potions, success))
