# finding length of string

# Using iterative method


def iterative_len_string(s):
    count = 0
    for i in range(len(s)):
        count += 1
        return count

# Using recursive method


def recursive_len_string(s):
    if s == "":
        return 0
    return 1 + recursive_len_string(s[1:])


print(recursive_len_string("siva"))
