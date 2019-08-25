# check a string is palindrome using recursion. But before validate the string.

def is_palindrome(s):
    def to_chars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
                print ans
        return ans

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            print s
            return s[0] == s[-1] and is_pal(s[1:-1])
    return is_pal(s)
