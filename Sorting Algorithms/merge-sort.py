# time complexity = O(n log n)
def merge(left, right, arr):
    i = j = k = 0

    # copy data to temporary arrays left[] and right[]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1

    # Checking if any element was left in the left array
    while i < len(left):
        arr[k] = left[i]
        i = i + 1
        k = k + 1

    # checking if any element was left in the right array
    while j < len(right):
        arr[k] = right[j]
        j = j + 1
        k = k + 1


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)


x = [3, 4, 1, 7, 5, 6, 9, 10]
merge_sort(x)
print(x)
