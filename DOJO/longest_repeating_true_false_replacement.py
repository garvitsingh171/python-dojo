def answerKey(string, k):

    def max_len(char):
        left = 0
        count = 0
        res = 0

        for right in range(len(string)):
            if string[right] != char:
                count += 1

            while count > k:
                if string[left] != char:
                    count -= 1
                left += 1

            res = max(res, right - left + 1)

        return res

    return max(max_len('T'), max_len('F'))


string = input()
k = int(input())

print(answerKey(string, k))
