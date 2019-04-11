# program to find longest length of substring.
# if s = "abcddef" - return len(abc) - 3


def lengthOfLongestSubstring(s):

    start, end = 0, 0
    current_set = set()
    to_return = 0
    for ch in s:
        if ch not in current_set:
            current_set.add(ch)
        else:
            to_return = max(to_return, end - start)
            while s[start] != ch:
                current_set.remove(s[start])
                start += 1
            start += 1
        end += 1
    to_return = max(to_return, end - start)
    return to_return



