def isBalanced(s):
    # Write your code here
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return 'NO'
            else:
                stack.pop()

    return 'YES' if not stack else 'NO'
