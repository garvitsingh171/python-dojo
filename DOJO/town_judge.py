# Town Judge

m = int(input("Enter the size of trust array: "))
n = int(input("Enter the number of people: "))
trust = []

for i in range(m):
    t = list(map(int, input(f"Enter the {i} trust element: ").split()))
    trust.append(t)

in_trust = [0] * (n+1)
out_trust = [0] * (n+1)

for a, b in trust:
    in_trust[b] += 1
    out_trust[a] += 1

judge = -1

for i in range(1, n+1):
    if in_trust[i] == n - 1 and out_trust[i] == 0:
        judge = i
        break

print(judge)
