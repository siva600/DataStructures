
# Insertion sort with O(n*n) complexity using swapping method.
#
# def insertion_sort(lst):
#     for i in range(1, len(lst)):
#         for j in range(i - 1, -1, -1):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#             else:
#                 break
#     return lst
#

# Insertion sort with O(n*n) complexity using shifting method. This method eliminates,
# the three steps involved in swapping method.
def insertion_sort_shifting(lst):
    for i in range(1, len(lst)):
        currentNumber = lst[i]
        print("currnet_number: ",currentNumber)
        for j in range(i-1, -1, -1):
            print("j: ", j)
            if lst[j] > currentNumber:
                print("lst[j]: ", lst[j])
                lst[j+1] = lst[j]
                print("lst[j+1] after :", lst[j+1])
                print("lst[j] afer: ", lst[j])
            else:
                lst[j+1] = currentNumber
                break
    return lst


lst = [3, 5, 4, 1, 0, -1]

# print(insertion_sort(lst))
print(insertion_sort_shifting(lst))
