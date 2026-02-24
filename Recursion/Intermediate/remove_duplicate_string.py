# Only for adjacent duplicate (not triplicate and not anything else)

def removeDuplicate(string):
    if len(string) <= 1:
        return string
    if string[0] == string[1]:
        return removeDuplicate(string[1:])
    return string[0] + removeDuplicate(string[1:])


string = input()

print(removeDuplicate(string))
