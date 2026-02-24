def TowerOfHanoi(n, fromRod, auxRod, toRod):
    if n == 0:
        return
    TowerOfHanoi(n-1, fromRod, auxRod, toRod)
    print('Disk', n, 'moved from', fromRod, 'to', toRod)
    TowerOfHanoi(n-1, auxRod, toRod, fromRod)


TowerOfHanoi(5, 'A', 'B', 'C')
