# '''
# Input: an integer
# Returns: an integer
# '''

# import time

# # to improve runtime, change to iterative solution
# # what about spacetime complexity....

# start_time = time.time()


# def eating_cookies(n, cache=None):
#     # start with base case
#     # negative value not valid way to eat cookies
#     if n < 0:
#         return 0
#         # getting to 0 means found way to eat cookies
#     elif n == 1 or n == 0:
#         return 1
#         # recursion not using cache
#     if cache == None:
#         return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
#         # create cache
#         # cache[n]= eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
#     else:
#         if cache[n]:
#             return cache[n]
#         else:
#             cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

#             return cache[n]


# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 5

# end_time = time.time()

# print(f"my runtime is...{end_time - start_time}  ")
# print(
#     f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")


# guided lecture
def eating_cookies(n, cache=None):
    print(n)
    # check for negative values
    if n < 0:
        return 0
    if n == 0:
        return 1
    # check if cache exiss
    # check if n is in cache
    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]

    cache[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

    return cache[n]


eating_cookies(4)
