def reverseString(string):
    if len(string) == 0:
        return string
    return reverseString(string[1:]) + string[0]


string = input()

print(reverseString(string))
