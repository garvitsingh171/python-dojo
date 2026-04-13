def pushDominos(dominos):
    n = len(dominos)

    forces = [0] * n

    force = 0
    for i in range(len(dominos)):
        if dominos[i] == 'R':
            force = n
        elif dominos[i] == 'L':
            force = 0
        else:
            force = max(force - 1, 0)
        forces[i] += force

    force = 0
    for i in range(len(dominos) - 1, -1, -1):
        if dominos[i] == 'L':
            force = n
        elif dominos[i] == 'R':
            force = 0
        else:
            force = max(force - 1, 0)
        forces[i] -= force

    res = []
    for f in forces:
        if f < 0:
            res.append('L')
        elif f > 0:
            res.append('R')
        else:
            res.append('.')

    return ''.join(res)


dominos = input()

print(pushDominos(dominos))
