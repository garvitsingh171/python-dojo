def count(nums, bound):
    count = 0
    curr = 0

    for num in nums:
        if num <= bound:
            curr += 1
            count += curr
        else:
            curr = 0

    return count


def count_subarrays(nums, left, right):
    return count(nums, right) - count(nums, left-1)


n = int(input())
left, right = list(map(int, input().split()))
arr = list(map(int, input().split()))

print(count_subarrays(arr, left, right))
