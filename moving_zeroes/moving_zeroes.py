'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    for i in range(len(arr)):
        print(i)
        if arr[i] == 0:
            zero = arr.pop(i)
            arr.append(zero)

    print(arr)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

 # use 2 points at beginning and end
    # if left pointer sees a zero and right poinst sees a non zero, swap
    # if the left sees a non-zero increment
    # if the right see a zero increment


def moving_zeros_optimized(arr):
    # left pointer at the beginning
    # right pointer at the end

    # loop until left and right pointers meet or right pointer passes left pointer (R< L)
    # swap situation:
    # left sees zero and right sees non-zero
    # swap the items
    # increment left
    # decrement right
    # non-swap situation
    # if left sees non-zero
    # increment left
    # if right sees zero
    # decrement right
