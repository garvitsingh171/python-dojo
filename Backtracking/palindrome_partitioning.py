def palindrome_partitioning(s):
    result = []

    def is_palindrome(string):
        return string == string[::-1]

    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return

        for end in range(start, len(s)):
            substring = s[start:end+1]

            if is_palindrome(substring):
                path.append(substring)
                backtrack(end+1, path)
                path.pop()

    backtrack(0, [])
    return result


s = input()

print(palindrome_partitioning(s))
