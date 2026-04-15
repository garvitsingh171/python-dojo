def successfulPairs(spells, potions, success):
    spells_with_index = sorted([(spell, i) for i, spell in enumerate(spells)])

    potions.sort()
    n = len(potions)

    right = n - 1

    res = [0] * len(spells)

    for spell, idx in spells_with_index:
        while right >= 0 and spell * potions[right] >= success:
            right -= 1

        res[idx] = n - (right + 1)

    return res


spells = list(map(int, input().split()))
potions = list(map(int, input().split()))
success = int(input())

print(successfulPairs(spells, potions, success))
