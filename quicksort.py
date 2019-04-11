# quick sort working technique.- e.g [33,15,10]
# Pick a pivot element - here 33
# partition the array to two sub arrays. 1st array of elements less than pivot,
#          second array of elements greater than pivot. Here - [15,10] + 33 + [ ]
#  then apply recursion for left array and right array again.
# e.g quick_sort([3,5,2,1,4])  - picking pivot as 3 , quick_sort([2,1]) + 3 + quick_sort([3,5,4])
# applying recursion for the left elements and right elements.

# average run time - O(nlogn)!.
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i >= pivot]
        # print("less array", less)
        # print("greater array", greater)
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10,5,2,3]))