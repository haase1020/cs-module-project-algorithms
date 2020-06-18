'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")


# list not best choice for efficiency. Following from guided lecture
def single_number_optimized(nums):
    # keep track of number of times an items occurs in input
    counts = {}

    # loop through inpu list O(n)
    for num in nums:
        # if item in counts
        if num in counts:
            del counts[num]

        else:
            # set item count to 1
            counts[num] = 1
    return counts[counts.keys()[0]]
    for k, v in counts.items():
        if v == 1:
            return k
