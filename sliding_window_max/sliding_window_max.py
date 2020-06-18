'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    if not nums or k < 1 or k > len(nums):
        return []

    output = []
    dq = []
    # notes:
    # length dq <= k
    # values stored are indexes
    # max contained dq[0]
    for i, num in enumerate(nums):
        if dq and dq[0] < i - k + 1:
            dq.pop(0)
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            output.append(nums[dq[0]])

    return output


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
