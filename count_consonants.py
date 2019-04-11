# Program to counts no.of consonants.
# i.e letter that is not a,e,i,o,u.


def count_consonants(s):
    vowels = "aeiou"
    consonants = []
    for ch in range(len(s)):
        if s[ch] not in vowels and s[ch].isalpha():
            consonants.append(s[ch])
    print(consonants)
    return len(consonants)

# recursive_count_consonants("abc")
#   recursive_count_consonants("bc")
#       recursive_count_consonants("c)


def recursive_count_consonants(s):
    vowels = "aeiou"
    if s == "":
        return 0
    if s[0].lower() not in vowels and s[0].isalpha():
        return 1 + recursive_count_consonants(s[1:])

    # returning 1 + recursive call to keep track of that call and
    # processing only remaining items but not first item.
    else:
        return recursive_count_consonants(s[1:])


string = "dajknsdakjqpoml.knpwqp"
print(count_consonants(string))
print(recursive_count_consonants(string))
