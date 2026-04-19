def letter_combination(digit):
    result = []

    phone = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def backtrack(path, index):
        if len(path) == len(digit):
            result.append(path)
            return

        letters = phone[digit[index]]

        for ch in letters:
            backtrack(path+ch, index+1)

    backtrack("", 0)
    return result


digit = input()

print(letter_combination(digit))
