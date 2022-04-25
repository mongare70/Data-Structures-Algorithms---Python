def quicksort(arr):
    qs(arr, 0, len(arr) - 1)


def qs(arr, l, r):
    if l >= r:
        return
    p = partition(arr, l, r)

    qs(arr, l, p - 1)
    qs(arr, p + 1, r)


def partition(arr, l, r):
    # choosing the last element as the pivot
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1

            # swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # swap arr[i+1] and arr[r]        
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


x = [3, 4, 1, 2, 5]
quicksort(x)
print(x)
