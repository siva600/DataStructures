# # d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11,
# #      'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,
# #      'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
# #
#
d = {chr(i+96): i for i in range(1,27)}
input = '1234'

l = []
for i in input:
    l.append(i)

s = set()
from itertools import combinations

comb = combinations(l, 2)
for i in list(comb):
    s.add(''.join(i))

comb = combinations(l, 1)
for i in list(comb):
    s.add(''.join(i))

result = []
for k, v in d.items():
    if str(v) in s:
        result.append(k)

result.sort()
print(s)
print(result)


#
# from itertools import combinations
#
#
# def message_decoding(input):
#     output = []
#     s = set()
#     my_lst = []
#
#     # using dictionary comprehension we get mapped values for alphabets.
#     d = {chr(i + 96): i for i in range(1, 27)}
#
#     # taking the input as list.
#     for i in input:
#         my_lst.append(i)
#
#     # obtain combinations of 2 digit message and add to set.
#     comb = combinations(my_lst, 2)
#     for i in comb:
#         s.add(''.join(i))
#
#     # obtain  combination of 1 digit message and add to set.
#     comb = combinations(my_lst, 1)
#     for k in comb:
#         s.add(''.join(k))
#
#     # obtain  combination of 3 digit message and add to set.
#     # comb = combinations(my_lst, 3)
#     # for k in comb:
#     #     if
#     #     s.add(''.join(k))
#
#     # Now match values in our set to our values in our dictionary which have value for each key.
#     for k, i in d.items():
#         if str(i) in s:
#             output.append(k)
#
#     output.sort()
#     return output
#
#
# message = '1234'
# print(message_decoding(message))
