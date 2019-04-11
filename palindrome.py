# l1 = [9, 9, 9, 9] #9999
# l1 = [int(i) for i in str(int(''.join([str(item) for item in l1])) + 1)]
# print(l1)
#
# l1 = [9, 9, 9, 9]
# print(''.join([str(item) for item in l1]))
# print(''.join(map(str, l1)))
#
# v1 = int(''.join(map(str, l1)))
# print(v1 + 1)
# s = ''.join([i for i in s if i.isalpha()]).replace(" ", "").lower()
# print(s == s[::-1])


def is_palind(s):
    i = 0
    j = len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1
    return True


s = "malayalam"
s = "Was it a cat I saw?"
print(is_palind(s))








