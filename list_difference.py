def find_missing(full_set, partial_set):
    missing_items = set(full_set) -set(partial_set)
    assert(len(missing_items)==1)
    return list(missing_items)[0]


def find_missing_xor(full_set, partial_set):
    print(full_set)
    print(partial_set)
    xor_sum = 0
    for num in full_set:
        xor_sum = xor_sum ^ num
        print(xor_sum)
    print("\n")
    for num in partial_set:
        xor_sum ^= num
        print(xor_sum)
    print("\n")
    return xor_sum


a = [2,3,4]
b = [2]
# print(find_missing(a, b))
print(find_missing_xor(a,b))
