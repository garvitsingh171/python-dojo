def numRescueBoat(people, limit):
    people.sort()

    low, high = 0, len(people) - 1
    boats = 0

    while low <= high:
        if people[low] + people[high] <= limit:
            low += 1
            high -= 1
        else:
            high -= 1

        boats += 1

    return boats


n, limit = map(int, input().split())
people = list(map(int, input().split()))

print(numRescueBoat(people, limit))
