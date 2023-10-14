# Given an array of N non-negative integers arr[] representing an elevation map
#  where the width of each bar is 1,
# compute how much water it is able to trap after raining


# define function to take array and return maxmum water
def maxWater(arr, n):
    # define storage
    water = 0
    for i in range(1, n - 1):
        # maximum in left
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        # maximum on right
        right = arr[i]
        for j in range(i + 1, n):
            right = max(right, arr[j])

    # feed into our algorithm
        water = water + (min(left, right) - arr[i])
    return water


# Driver code
if __name__ == "__main__":
    arr = [3, 0, 0, 2, 0, 4]
    n = len(arr)

    print(maxWater(arr, n))
