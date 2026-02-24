def lastOccurence(arr, x, count):
    if len(arr) == 0:
        return
    lastOccurence(arr[1:], x, count+1)
    if arr[0] == x:
        return count


n = int(input())
arr = list(map(int, input().split()))
x = int(input())
count = 1

print(lastOccurence(arr, x, count))
