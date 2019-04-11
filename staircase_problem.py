# No.of ways we can climb the staircase with fixed no.of steps either 1 or 2 at a each time.
#  solution:
# If N =1, 1 <- {[1,0]}
# If N= 2, 2 <- {[2,1,0], [2,0]}
# If N= 3, 3<- {[3,2,1,0], [3,2,0], [3,1,0]}
# If N=4,  4<- {[4,3,2,1,0], [4,3,2,0], [4,3,1,0], [4,2,1,0], [4,2,0]}

# num_ways(N) = num_ways(N-1) + num_ways(N-2)
#
# num_ways(0) = 1
# num_ways(1) = 1


my_storage = {}

def num_ways(n):
    if n in my_storage:
        return my_storage[n]
    if n == 1 or n==0:
        return 1
    else:
        ways = num_ways(n-1) + num_ways(n-2)
    my_storage[n] = ways
    return ways

# when X = {1,3,5} fixed steps we can climb the staircase for n steps.
# can be solved as num_ways(n) = num_ways(n-1) + num_ways(n-3) + num_ways(n-5)
# but for 2 steps, num_ways(n-3) = num_ways(2-3) = num_ways(-1) NOT VALID. so check n-i >0.

my_storage_x = {}


def num_ways_X(n):
    if n in my_storage_x:
        return my_storage_x[n]
    if n == 0:
        return 1
    total = 0
    for i in {1, 3, 5}:
        if (n-i) >= 0:
            total += num_ways_X(n-i)
        my_storage_x[n] = total
    return total


print(num_ways(50))
print(num_ways_X(100))
