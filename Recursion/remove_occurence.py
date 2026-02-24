def removeOccurence(string, elem):
    if len(string) == 0:
        return ""
    if string[0] == elem:
        return removeOccurence(string[1:], elem)
    else:
        return string[0] + removeOccurence(string[1:], elem)


string = input()
elem = input()
print(removeOccurence(string, elem))
