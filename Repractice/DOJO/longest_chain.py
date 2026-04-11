def longest_chain(pairs):
    pairs.sort(key=lambda x: x[1])

    prev_right = float('-inf')
    count = 0

    for left, right in pairs:
        if left > prev_right:
            count += 1
            prev_right = right

    return count


pairs = []
n = int(input())
for _ in range(n):
    pairs.append(list(map(int, input().split())))

print(pairs)

print(longest_chain(pairs))
