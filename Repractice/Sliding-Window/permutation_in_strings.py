def permutation_in_strings(s1, s2):
    if len(s1) > len(s2):
        return False

    win_1 = [0] * 26
    win_2 = [0] * 26

    for ch in s1:
        win_1[ord(ch) - ord('a')] += 1

    for i in range(len(s1)):
        win_2[ord(s2[i]) - ord('a')] += 1

    if win_1 == win_2:
        return True

    for i in range(len(s1), len(s2)):
        win_2[ord(s2[i]) - ord('a')] += 1
        win_2[ord(s2[i - len(s1)]) - ord('a')] -= 1

        if win_1 == win_2:
            return True

    return False


s1 = input()
s2 = input()

print(permutation_in_strings(s1, s2))
