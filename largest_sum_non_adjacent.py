# Function to return max sum such that
# no two elements are adjacent
def find_max_sum(arr):
    incl = 0
    excl = 0

    for i in arr:
        # Current max excluding i (No ternary in
        # Python)
        new_excl = excl if excl > incl else incl

        # Current max including i
        incl = excl + i
        excl = new_excl

        # return max of incl and excl
    return (excl if excl > incl else incl)


lst = [2, 4, 6, 2, 1, 4, 5, 7]
lst2 = [7, 1, 0, 0, 0, 0, 0, 0]
lst3 = [5, 1, 1, 5]
lst4 = [5, 1, 4, 5]
lst5 = [5, 1, 5, 4]


print(find_max_sum(lst2))
