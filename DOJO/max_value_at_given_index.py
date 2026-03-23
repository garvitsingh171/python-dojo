def maxValueArray(n, index, maxSum):

    def calc(x):

        left_len = index
        if x > left_len:
            left_sum = ((x-1 + x-left_len) * left_len) // 2
        else:
            left_sum = ((x-1+1) * (x-1) // 2) + (left_len - (x-1))

        right_len = n - index - 1
        if x > right_len:
            right_sum = ((x-1 + x-right_len) * right_len) // 2
        else:
            right_sum = ((x-1+1) * (x-1) // 2) + (right_len - (x-1))

        return left_sum + right_sum + x

    low, high = 1, maxSum
    ans = 1

    while low <= high:
        mid = (low + high) // 2

        if calc(mid) <= maxSum:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans


n = int(input())
index = int(input())
maxSum = int(input())

print(maxValueArray(n, index, maxSum))
