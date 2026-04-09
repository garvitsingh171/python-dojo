def longestChain(pairs):
    pairs.sort(key=lambda x: x[1])

    curr_end = float('-inf')
    count = 0

    for left, right in pairs:
        if left > curr_end:
            count += 1
            curr_end = right

    return count


# Input
n = int(input())
pairs = []

for _ in range(n):
    left, right = map(int, input().split())
    pairs.append([left, right])

print(longestChain(pairs))
