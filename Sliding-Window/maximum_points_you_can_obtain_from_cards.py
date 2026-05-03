def maxScore(cardPoints, k):
    n = len(cardPoints)
    size = n - k

    total = sum(cardPoints)

    if n == k:
        return total

    win_sum = sum(cardPoints[:size])
    min_sum = win_sum

    left = 0

    for right in range(size, n):
        win_sum += cardPoints[right]
        win_sum -= cardPoints[left]

        if win_sum < min_sum:
            min_sum = win_sum

        left += 1

    return total - min_sum


cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3

print(maxScore(cardPoints, k))

# Technique = Sliding Window
# TC = O(n)
# SC = O(1)
