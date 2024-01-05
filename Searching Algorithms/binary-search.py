import math


def search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = math.floor((left + right) / 2)

        if arr[mid] == target:
            return mid

        elif target < arr[mid]:
            right = mid - 1

        else:
            left = mid + 1

    return -1


# uses a sorted array
array1 = [1, 3, 4, 7, 8, 9, 10, 20]
print(search(array1, 4))
