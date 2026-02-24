def climb_stairs(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return climb_stairs(n-1) + climb_stairs(n-2)


n = int(input())

print(climb_stairs(n))
