#  find the first missing positive integer in linear time and constant space.
#  In other words, find the lowest positive integer that does not exist in the array.
#  The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.


def find_least_positive(input_list):
    input_list.sort()
    status = 0
    # below considering max item of list and checking our main list with
    # iterator values.
    # considering status for missing value found or not found.
    for i in range(1, input_list[-1]+1):
        if i not in input_list:
            status = 1
            print(i)
    if status == 0:
        print(input_list[-1]+1)


l = [1, 2, 0]
find_least_positive(l)
