# Given an array of N non-negative integers arr[] representing an elevation map
#  where the width of each bar is 1,
# compute how much water it is able to trap after raining


# define function to take array and return maxmum water
def maxWater(arr, n):
    water = 0
    for i in range(1, n - 1):

        left = i - 1

        right = i + 1
        
    water = water + (min(left, right) - arr[i])
    return water


# Driver code
if __name__ == "__main__":
    arr = [2, 0, 2]
    n = len(arr)

    print(maxWater(arr, n))
