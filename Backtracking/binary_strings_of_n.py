def binaryStrings(n):
    result = []

    def backtrack(path):

        if len(path) == n:
            result.append(''.join(path))
            return

        path.append('0')
        backtrack(path)
        path.pop()

        path.append('1')
        backtrack(path)
        path.pop()

    backtrack([])
    return result


n = int(input())

print(binaryStrings(n))
