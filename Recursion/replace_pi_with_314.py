def replacePi(string):
    if len(string) == 0:
        return ""
    if string[0] == 'p' and string[1] == 'i':
        return string.replace('pi', '3.14')
    else:
        return replacePi(string[1:])


string = input()

print(replacePi(string))
