# find the first recurring character in the string.
def first_recurring_nohashmap(s):
    s = list(s)
    for index, ch in enumerate(s):
        if ch in s[index+1:]:
            return "First Recursion {}".format(ch)


def first_recurring_hashmap(s):
    hash_map = {}
    for ch in s:
        if ch in hash_map:
            return "First recurring using hash_map is {}".format(ch)
        hash_map[ch] = 1
        print(hash_map)
    return None


print(first_recurring_nohashmap("DBCABA"))

print(first_recurring_hashmap("DBCABA"))


