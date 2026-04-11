def prefix(expression):
    stack = []

    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.append(token)
        else:
            op2 = stack.pop()
            op1 = stack.pop()

            new_exp = token + ' ' + op1 + ' ' + op2

            stack.append(new_exp)

    return stack


expression = input()

print(prefix(expression))
