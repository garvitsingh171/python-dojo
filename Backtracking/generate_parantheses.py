def parantheses(n):
    result = []

    def backtrack(path, open_count, close_count):

        if len(path) == 2*n:
            return result.append(path)

        if open_count < n:
            backtrack(path + "(", open_count+1, close_count)

        if close_count < open_count:
            backtrack(path + ")", open_count, close_count+1)

    backtrack("", 0, 0)
    return result


n = int(input())

print(parantheses(n))
