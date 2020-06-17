# Single Number

Given a non-empty array of integers where every element appears twice except for one. Find that single number. You may assume that there will _always_ be _one_ odd-number-out and every other number in the input shows up exactly twice.

## Examples

```
Sample input: [2, 2, 1]
Expected output: 1
```

```
Sample iput: [4, 1, 2, 1, 2]
Expected output: 4
```

Can you implement a solution that finds the single number in _one_ pass through the input array with `O(1)` space complexity?

## Testing

Run the test file by executing `python test_single_number.py`.

# UPER:

# understand: array of ints. Only one element appears once. All other numbers appear twice. Can be negative ints? No blanks in array

# plan: arr param. use count method for item in array. If == 1 then single item

# execute (see code)

# reflect
